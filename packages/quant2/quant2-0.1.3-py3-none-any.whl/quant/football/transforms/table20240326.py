# from: base
# data type: FootballDatasetV1
# model type: STNetV3
import numpy as np
from typing import Union
from quant.football.data.preprocessing import get_scale_params, scale
from quant.football.data.utils import label_encoder, odds_data_avg_max_min, one_hot_encoder


def parse_attrs_data(data: dict):
    data = data["titan"]

    keys = [
        "match_id",
        "match_time",
        "match_state",
        "season_name",
        "home_score",
        "visiting_score",
        "home_half_score",
        "visiting_half_score",
        "home_team_name",
        "visiting_team_name",
    ]

    # 10: 10(n-key) * 1(none) + 0(none)
    xs = [data[k] for k in keys]
    return xs


def parse_event_data(data: dict):
    data = data["events"]

    keys = [
        ("goalIn", 0),  # 进球
        ("changePlayer", 1),  # 换人
        ("yellowCard", 2),  # 黄牌
        ("redCard", 3),  # 红牌
        ("ownGoal", 4),  # 乌龙
        ("penaltyKick", 5),  # 点球
        ("penaltyKickMiss", 6),  # 射失点球
        ("doubleYellowToRed", 7),  # 两黄变红
    ]

    xs_home = np.zeros((6, len(keys)), dtype=int)
    xs_away = np.zeros((6, len(keys)), dtype=int)
    for event in data:
        for key, idx in keys:
            if key in event:
                kind = event["kind"].lower()
                cycle = event["time"][:-1].split("+")[0]
                cycle = max(0, (int(cycle) - 1) // 15)
                if cycle > 5:
                    break
                if kind == "home":
                    xs_home[cycle][idx] += 1
                if kind == "away":
                    xs_away[cycle][idx] += 1
                break

    # 96: 8(n-key) * 6(n-cycle) + 8(n-key) * 6(n-cycle)
    xs = xs_home.reshape(-1).tolist() + xs_away.reshape(-1).tolist()
    return xs


def parse_odds_data(data: dict):
    first_1x2 = [v[-1] for v in data["odds_1x2"].values() if v]
    first_overunder = [v[-1] for v in data["odds_overunder"].values() if v]
    first_1x2 = odds_data_avg_max_min(first_1x2)
    first_overunder = odds_data_avg_max_min(first_overunder)
    # 18: 3(avg-max-min) * 3(1x2) + 3(avg-max-min) * 3(overunder)
    xs = first_1x2 + first_overunder
    return xs


def extract_features(data: dict):
    attrs_data = parse_attrs_data(data["mapping_match"])
    event_data = parse_event_data(data["event_titan"])
    odds_data = parse_odds_data(data["bets_titan"])
    # 124: 10(attrs) + 96(event) + 18(odds)
    xs = attrs_data + event_data + odds_data
    return xs


def check_samples(data: list[list]):
    cycle_size = 8
    good_data, bad_data, bad_info = [], [], []
    for sample in data:
        a = int(sample[6]) + int(sample[7])  # 半场
        b = int(sample[4]) + int(sample[5])  # 全场
        a1 = sum([sum(sample[10+i:34:cycle_size]) for i in [0, 4, 5]])
        b1 = sum([sum(sample[10+i:58:cycle_size]) for i in [0, 4, 5]])
        a2 = sum([sum(sample[58+i:82:cycle_size]) for i in [0, 4, 5]])
        b2 = sum([sum(sample[58+i:106:cycle_size]) for i in [0, 4, 5]])
        if a == (a1 + a2) and b == (b1 + b2):
            good_data.append(sample)
            continue
        bad_data.append(sample)
        bad_info.append((a, b, a1, b1, a2, b2))
    return good_data, bad_data, bad_info


def filter_samples(data: list[list], limit: int = 5):
    team_idxs = [8, 9]

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
    # [0:4] : [比赛ID,比赛时间,比赛状态,联赛名]
    # [4:8] : [主队得分,客队得分,主队半场得分,客队半场得分]
    # [8:10] : [主队名称,客队名称]
    # [10:58] : [进球,换人,黄牌,红牌,乌龙,点球,射失点球,两黄变红]x6
    # [58:106] : [进球,换人,黄牌,红牌,乌龙,点球,射失点球,两黄变红]x6
    # [106:124] : [初赔均值,初赔最大,初赔最小]x[胜平负,进球数]
    cycle_size = 8
    assert -1 < stages < 7
    sub_len = cycle_size * stages

    qkeys = []
    scores = []
    team_home = []
    team_away = []
    features_in = []
    for sample in data:
        qkeys.append(sample[0:4])
        scores.append(sample[4:8])
        team_home.append(sample[8])
        team_away.append(sample[9])
        features_in.append(sample[10:(10 + sub_len)] +
                           sample[58:(58 + sub_len)] +
                           sample[106:124])

    if isinstance(encoder, str):
        # method: label, one_hot
        method = encoder
        if method == "label":
            encoder = label_encoder(team_home + team_away)
        elif method == "one_hot":
            encoder = one_hot_encoder(team_home + team_away)
        else:
            raise NotImplementedError(f"Not supported <{encoder=}>.")
    assert isinstance(encoder, dict), f"{type(encoder)=} is not <dict>."

    X, Y, Z = [], [], []
    for _home, _away, _vals, _outs, _qkey in zip(team_home, team_away, features_in, scores, qkeys):
        if _home not in encoder or _away not in encoder or any([v < 0 for v in _vals]):
            continue
        X.append(encoder[_home] + encoder[_away] + _vals)
        if whole:
            Y.append(min(nc - 1, int(_outs[0]) + int(_outs[1])))
        else:
            Y.append(min(nc - 1, int(_outs[2]) + int(_outs[3])))
        Z.append(_qkey + [0])

    if isinstance(transforms, str):
        # method: standard, minmax, maxabs
        method = transforms
        n_features = len(X[0])

        _XT = [[] for _ in range(n_features)]
        for sample in X:
            for idx, val in enumerate(sample):
                _XT[idx].append(val)

        transforms = [None for _ in range(n_features)]
        for idx in range(encoder["__dim__"] * 2, n_features):
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
