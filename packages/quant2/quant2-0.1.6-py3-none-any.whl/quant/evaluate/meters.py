import pandas as pd
import plotly.express as px
from collections import defaultdict
from quant.evaluate.utils import filter_odds_by_time, compute_bet_overunder
from quant.football.data.utils import time_secs2str
from quant.utils.io import load_pkl


def compute_acc(results, acc_by="mon", threshold=0.5, eps=1e-5):
    ends = {"yea": 4, "mon": 7, "day": 10}
    assert acc_by in ends, f"<{acc_by=}> not in {ends.keys()}"

    if isinstance(results, str):
        results = load_pkl(results)

    # "yyyy-mm-dd hh:mm:ss"
    end = ends[acc_by]

    counts = {}
    for row in results:
        # row: [y, z, y_, probs]
        # z: [比赛ID,比赛时间,比赛状态,...,比赛进度,残差还原]
        y, z, y_, probs = row

        flag = time_secs2str(int(z[1]))[:end]

        a, b, c = counts.get(flag, (0, 0, 0))
        if probs[y_] >= threshold:
            a = a + 1 if y == y_ else a
            counts[flag] = (a, b + 1, c + 1)
        else:
            counts[flag] = (a, b, c + 1)

    counts = [(k, a, b, c, a / (b + eps), b / (c + eps)) for k, (a, b, c) in counts.items()]
    return sorted(counts, key=lambda x: x[0])


def compute_ret(results, ret_by="mon", threshold=0.5, eps=1e-5):
    # TODO
    pass


def group_compute_acc(results, group_by=-2, acc_by="mon", threshold=0.5):
    if isinstance(results, str):
        results = load_pkl(results)

    group_data = defaultdict(list)
    for row in results:
        # row: [y, z, y_, probs]
        # z: [比赛ID,比赛时间,比赛状态,...,比赛进度,残差还原]
        point = f"{float(row[1][group_by])+0.01:4.1f}"
        group_data[point].append(row)

    data = []
    for k, v in group_data.items():
        counts = compute_acc(v, acc_by=acc_by, threshold=threshold)
        data.extend([(k,) + row for row in counts])

    data = sorted(data, key=lambda x: x[0])
    columns = ["time", "flag", "correct", "subset", "total", "acc", "rate"]
    df = pd.DataFrame(data, columns=columns)

    df["date"] = pd.to_datetime(df["flag"])
    df["day_number"] = df["date"].dt.strftime("%d")
    df["week_number"] = df["date"].dt.strftime("%W")
    df["month_number"] = df["date"].dt.strftime("%m")
    return df


def plot_df(df, x="time", y="acc", color="flag"):
    fig = px.line(df, x=x, y=y, color=color, markers=True)
    fig.show()
