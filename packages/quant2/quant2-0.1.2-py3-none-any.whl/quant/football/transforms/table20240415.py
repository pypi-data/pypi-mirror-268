# from: base
# data type: FootballDatasetV2
# model type: STNetV4
import numpy as np
from typing import Union
from quant.football.data.preprocessing import get_scale_params, scale
from quant.football.data.utils import convert_odds_data, label_encoder


def sequence_stats(data: list):
    assert len(data) > 1

    if isinstance(data[0], str):
        data = [float(x) for x in data]

    data = np.asarray(data)

    x_med = np.median(data).item()
    x_mea = data.mean().item()
    x_max = data.max().item()
    x_min = data.min().item()

    # 5: 5(中位数,均值,最大,最小,范围)
    return [x_med, x_mea, x_max, x_min, x_max - x_min]


def odds_data_to_stats(data: list[list]):
    # data = [['77', '1-2', '1.60', '3.5', '0.47', '10-02 00:39', '滚']]
    data = convert_odds_data(data)

    x1 = sequence_stats([row[2] for row in data])
    x2 = sequence_stats([row[3] for row in data])
    x3 = sequence_stats([row[4] for row in data])

    # 15: 5(统计量) * 3(赔率/盘口)
    return x1 + x2 + x3


def parse_titan_data(data: dict):
    keys = [
        "match_id",
        "match_time",
        "match_state",
        "season_name",
        "home_team_name",
        "visiting_team_name",
        "home_score",
        "visiting_score",
        "home_half_score",
        "visiting_half_score",
        "season_id",
        "home_team_id",
        "visiting_team_id",
    ]

    # 13: 13(n-key)
    vals = [data[k] for k in keys]
    return vals


def parse_event_data(data: list):
    keys = [
        ("goalIn", 0),  # 进球
        ("changePlayer", 1),  # 换人
        ("yellowCard", 2),  # 黄牌
        ("redCard", 3),  # 红牌
        ("ownGoal", 4),  # 乌龙
        ("penaltyKick", 5),  # 点球
        ("penaltyKickMiss", 6),  # 射失点球
        ("doubleYellowToRed", 7),  # 两黄变红
        ("videoReferee", 8),  # 视频裁判
    ]

    n_data, n_keys = len(data), len(keys)
    mat = np.zeros((n_data, n_keys * 2), dtype=int)

    for nrow, event in enumerate(data):
        for key, ncol in keys:
            if key in event:
                kind = event["kind"].lower()
                etime = int(event["time"][:-1].split("+")[0])
                ncol = ncol if kind == "home" else ncol + n_keys
                mat[nrow, ncol] = etime  # [1, 90]
                break

    # 1: [matrix[n,9+9]]
    return [mat]


def parse_round_data(data: dict):
    round_num = int(data["round_num"])

    if round_num < 3:
        vals = [1, 0, 0, 0]
    elif round_num < 6:
        vals = [0, 1, 0, 0]
    elif round_num < 9:
        vals = [0, 0, 1, 0]
    else:
        vals = [0, 0, 0, 1]

    # 4: 4(n-mode)
    return vals


def parse_odds_data(data: dict):
    first_1x2 = [v[-1] for v in data["odds_1x2"].values() if v]
    first_overunder = [v[-1] for v in data["odds_overunder"].values() if v]

    first_1x2 = odds_data_to_stats(first_1x2)
    first_overunder = odds_data_to_stats(first_overunder)

    # 30: 15(1x2) + 15(overunder)
    vals = first_1x2 + first_overunder
    return vals


def extract_features(section: dict):
    titan_data = parse_titan_data(section["mapping_match"]["titan"])
    event_data = parse_event_data(section["event_titan"]["events"])
    round_data = parse_round_data(section["round_info"])
    odds_data = parse_odds_data(section["bets_titan"])
    # 48: 13(titan) + 1(event:matrix) + 4(round) + 30(odds)
    sample = titan_data + event_data + round_data + odds_data
    return sample


def check_samples(data: list[list]):
    cycle_size = 9

    ncols = [0, 4, 5] + [cycle_size + i for i in [0, 4, 5]]

    good_data, bad_data, bad_info = [], [], []
    for sample in data:
        a1 = int(sample[8]) + int(sample[9])  # 半场: 主队+客队
        b1 = int(sample[6]) + int(sample[7])  # 全场: 主队+客队
        a2 = ((1 <= sample[13]) & (sample[13] <= 45))[:, ncols].sum().item()
        b2 = ((1 <= sample[13]) & (sample[13] <= 90))[:, ncols].sum().item()
        if a1 == a2 and b1 == b2:
            good_data.append(sample)
            continue
        bad_data.append(sample)
        bad_info.append((a1, b1, a2, b2))
    return good_data, bad_data, bad_info


def filter_samples(data: list[list], limit: int = 5):
    team_idxs = [11, 12]

    counts = {}
    for row in data:
        for idx in team_idxs:
            name = row[idx]
            if name in counts:
                counts[name] += 1
            else:
                counts[name] = 1

    _data = []
    for row in data:
        if any([counts[row[idx]] < limit for idx in team_idxs]):
            continue
        _data.append(row)
    return _data


def export_dataset(data: list[list], points: list[float], lbacks: list[int], encoder: Union[str, dict], whole: bool, nc: int, transforms: Union[str, list], prediction_method: str = "incremental"):
    # [0:6] : [比赛ID,比赛时间,比赛状态,联赛名,主队名,客队名]
    # [6:10] : [主队得分,客队得分,主队半场得分,客队半场得分]
    # [10:13] : [联赛ID,主队ID,客队ID]
    # [13:14] : [matrix[n,9+9]]
    # [14:18] : [赛季轮数]
    # [18:48] : [15+15]
    cycle_size = 9
    assert max(points) < 90
    assert min(points) > max(lbacks)

    qkeys = []
    scores = []
    season_id = []
    team_home = []
    team_away = []
    features_in = []
    for sample in data:
        for point in points:
            game_time = point / 90 if whole else point / 45
            qkeys.append(sample[0:6])
            scores.append(sample[6:10])
            season_id.append(sample[10])
            team_home.append(sample[11])
            team_away.append(sample[12])
            features_in.append(fn_look_backs(sample[13], point, lbacks) +
                               sample[14:48] + [game_time, 1.0 - game_time])

    if isinstance(encoder, str):
        method = encoder
        if method == "label":
            encoder = {
                "season": label_encoder(season_id),
                "team": label_encoder(team_home + team_away),
            }
        else:
            raise NotImplementedError(f"Not supported <{encoder=}>.")
    assert isinstance(encoder, dict), f"{type(encoder)=} is not <dict>."

    X, Y, Z = [], [], []
    for _season, _home, _away, _vals, _outs, _qkey in zip(season_id, team_home, team_away, features_in, scores, qkeys):
        if _season not in encoder["season"] or _home not in encoder["team"] or _away not in encoder["team"]:
            continue

        # 进球,换人,黄牌,红牌,乌龙,点球,射失点球,两黄变红,视频裁判
        _home_score = sum([_vals[i] for i in [0, 4, 5]])
        _away_score = sum([_vals[cycle_size + i] for i in [0, 4, 5]])
        _curr_score = [_home_score + _away_score, _home_score, _away_score]

        base_goals = _curr_score[0] if prediction_method == "incremental" else 0

        X.append(encoder["season"][_season] + encoder["team"][_home] + encoder["team"][_away] + _vals + _curr_score)
        if whole:
            Y.append(min(nc - 1, int(_outs[0]) + int(_outs[1]) - base_goals))
        else:
            Y.append(min(nc - 1, int(_outs[2]) + int(_outs[3]) - base_goals))
        Z.append(_qkey + _outs + [base_goals])

    if isinstance(transforms, str):
        method = transforms
        n_features = len(X[0])

        _XT = [[] for _ in range(n_features)]
        for sample in X:
            for idx, val in enumerate(sample):
                _XT[idx].append(val)

        transforms = [None for _ in range(n_features)]
        for idx in range(encoder["season"]["__dim__"] + encoder["team"]["__dim__"] * 2, n_features):
            transforms[idx] = get_scale_params(_XT[idx], method)
    assert isinstance(transforms, list), f"{type(transforms)=} is not <list>."

    _X = []
    for sample in X:
        _sample = []
        for val, args in zip(sample, transforms):
            if args is not None:
                _sample.append(scale(val, *args))
            else:
                _sample.append(val)
        _X.append(_sample)
    X = _X

    return X, Y, Z, lbacks, encoder, whole, nc, transforms, prediction_method


def fn_look_backs(mat: np.ndarray, point: float, lbacks: list[int]):
    vals = ((1 <= mat) & (mat < point)).sum(axis=0).tolist()
    for lback in lbacks:
        vals += ((point - lback <= mat) & (mat < point)).sum(axis=0).tolist()
    return vals
