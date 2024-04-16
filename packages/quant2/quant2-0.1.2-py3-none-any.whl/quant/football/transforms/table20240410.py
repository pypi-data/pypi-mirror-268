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

    x_len = len(data)
    x_sum = sum(data)
    x_max = max(data)
    x_min = min(data)
    return [x_sum / x_len, x_max, x_min, x_max - x_min, x_len]


def odds_data_to_stats(data: list[list]):
    # data = [['77', '1-2', '1.60', '3.5', '0.47', '10-02 00:39', '滚']]
    data = convert_odds_data(data)
    x1 = sequence_stats([row[2] for row in data])
    x2 = sequence_stats([row[3] for row in data])
    x3 = sequence_stats([row[4] for row in data])
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

    count_home = np.zeros((6, len(keys)), dtype=int)
    count_away = np.zeros((6, len(keys)), dtype=int)
    for event in data:
        for key, idx in keys:
            if key in event:
                kind = event["kind"].lower()
                cycle = event["time"][:-1].split("+")[0]
                cycle = max(0, (int(cycle) - 1) // 15)
                if cycle > 5:
                    break
                if kind == "home":
                    count_home[cycle][idx] += 1
                if kind == "away":
                    count_away[cycle][idx] += 1
                break

    # 108: 9(n-key) * 6(n-cycle) + 9(n-key) * 6(n-cycle)
    vals = count_home.reshape(-1).tolist() + count_away.reshape(-1).tolist()
    return vals


def parse_round_data(data: dict):
    round_type = data["round_type"].strip()
    round_num = int(data["round_num"])

    assert round_type in ("联赛", "杯赛"), f"Not supported <{round_type=}>."

    vals = [0, 0, 0, 0, 0]
    vals[0] = 1 if round_type == "联赛" else 0
    vals[1] = 1 if round_type == "杯赛" else 0
    vals[2] = 1 if round_num >= 3 else 0
    vals[3] = 1 if round_num >= 6 else 0
    vals[4] = 1 if round_num >= 9 else 0

    # 5: 5(n-mode)
    return vals


def parse_odds_data(data: dict):
    first_1x2 = [v[-1] for v in data["odds_1x2"].values() if v]
    first_overunder = [v[-1] for v in data["odds_overunder"].values() if v]

    first_1x2 = odds_data_to_stats(first_1x2)
    first_overunder = odds_data_to_stats(first_overunder)

    # 30: 5(avg+max+min+range+len) * 3(1x2) + 5(avg+max+min+range+len) * 3(overunder)
    vals = first_1x2 + first_overunder
    return vals


def extract_features(section: dict):
    titan_data = parse_titan_data(section["mapping_match"]["titan"])
    event_data = parse_event_data(section["event_titan"]["events"])
    round_data = parse_round_data(section["round_info"])
    odds_data = parse_odds_data(section["bets_titan"])
    # 156: 13(titan) + 108(event) + 5(round) + 30(odds)
    sample = titan_data + event_data + round_data + odds_data
    return sample


def check_samples(data: list[list]):
    cycle_size = 9
    good_data, bad_data, bad_info = [], [], []
    for sample in data:
        a = int(sample[8]) + int(sample[9])  # 半场: 主队+客队
        b = int(sample[6]) + int(sample[7])  # 全场: 主队+客队
        a1 = sum([sum(sample[13+i:40:cycle_size]) for i in [0, 4, 5]])
        b1 = sum([sum(sample[13+i:67:cycle_size]) for i in [0, 4, 5]])
        a2 = sum([sum(sample[67+i:94:cycle_size]) for i in [0, 4, 5]])
        b2 = sum([sum(sample[67+i:121:cycle_size]) for i in [0, 4, 5]])
        if a == (a1 + a2) and b == (b1 + b2):
            good_data.append(sample)
            continue
        bad_data.append(sample)
        bad_info.append((a, b, a1, b1, a2, b2))
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


def export_dataset(data: list[list], stages: int, encoder: Union[str, dict], whole: bool, nc: int, transforms: Union[str, list]):
    # [0:6] : [比赛ID,比赛时间,比赛状态,联赛名,主队名,客队名]
    # [6:10] : [主队得分,客队得分,主队半场得分,客队半场得分]
    # [10:13] : [联赛ID,主队ID,客队ID]
    # [13:67] : [进球,换人,黄牌,红牌,乌龙,点球,射失点球,两黄变红,视频裁判]x6
    # [67:121] : [进球,换人,黄牌,红牌,乌龙,点球,射失点球,两黄变红,视频裁判]x6
    # [121:126] : [联赛,杯赛,赛季已过3轮,赛季已过6轮,赛季已过9轮]
    # [126:156] : [平均,最大,最小,范围,数量]x[6初赔]
    cycle_size = 9
    assert -1 < stages < 7
    sub_len = cycle_size * stages

    qkeys = []
    scores = []
    season_id = []
    team_home = []
    team_away = []
    features_in = []
    for sample in data:
        qkeys.append(sample[0:6])
        scores.append(sample[6:10])
        season_id.append(sample[10])
        team_home.append(sample[11])
        team_away.append(sample[12])
        features_in.append(sample[13:(13 + sub_len)] +
                           sample[67:(67 + sub_len)] +
                           sample[121:156])

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

        _home_score = sum([sum(_vals[i:sub_len:cycle_size]) for i in [0, 4, 5]])
        _away_score = sum([sum(_vals[sub_len:][i:sub_len:cycle_size]) for i in [0, 4, 5]])
        _curr_score = [_home_score + _away_score, _home_score, _away_score]  # 当前总进球数,主队进球数,客队进球数

        X.append(encoder["season"][_season] + encoder["team"][_home] + encoder["team"][_away] + _vals + _curr_score)
        if whole:
            Y.append(min(nc - 1, int(_outs[0]) + int(_outs[1]) - _curr_score[0]))
        else:
            Y.append(min(nc - 1, int(_outs[2]) + int(_outs[3]) - _curr_score[0]))
        Z.append(_qkey + _outs + [_curr_score[0]])

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

    return X, Y, Z, stages, encoder, whole, nc, transforms
