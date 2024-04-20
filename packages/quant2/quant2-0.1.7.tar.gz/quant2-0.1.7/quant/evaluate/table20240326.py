from pathlib import Path
from quant.evaluate.utils import filter_odds_by_time, compute_bet_overunder, compute_bet_overunder_ret
from quant.utils.io import load_json, load_pkl


def betting_experiment(results, sections, whole=True, time_range=(76, 80), ret_thr=1.2, ret_conf_thr=0.7):
    if isinstance(results, str):
        suffix = Path(results).suffix
        if suffix == ".json":
            results = load_json(results)
        elif suffix == ".pkl":
            results = load_pkl(results)
        else:
            raise NotImplementedError(f"Not supported <{suffix=}>.")

    if isinstance(sections, str):
        suffix = Path(sections).suffix
        if suffix == ".json":
            sections = load_json(sections)
        elif suffix == ".pkl":
            sections = load_pkl(sections)
        else:
            raise NotImplementedError(f"Not supported <{suffix=}>.")

    if isinstance(sections, list):
        sections = {s["mapping_match"]["titan"]["match_id"]: s for s in sections}

    total_bet = 0
    correct_bet = 0
    correct_bet_ret = 0
    for row in results:
        # row = [y, z, y_, probs]
        # z = [比赛ID,比赛时间,比赛状态,联赛名,...,残差还原]
        match_id, probs = row[1][0], row[3]

        z = row[1]
        if z[-1] > 0:
            probs = [0] * z[-1] + probs

        section = sections[match_id]

        titan = section["mapping_match"]["titan"]
        if whole:
            score = int(titan["home_score"]) + int(titan["visiting_score"])
        else:
            score = int(titan["home_half_score"]) + int(titan["visiting_half_score"])

        bet_odds = []
        for _, odds_data in section["bets_titan"]["odds_overunder"].items():
            bet_odds.extend(filter_odds_by_time(odds_data, time_range))

        if len(bet_odds) < 1:
            continue

        for odds in sorted(bet_odds, key=lambda x: int(x[0])):
            bet_p, bet_c_over, bet_c_under, bet_e = compute_bet_overunder(probs, odds, ret_thr, ret_conf_thr)[:4]
            if bet_e != "none":
                break

        a, b, c = compute_bet_overunder_ret(score, bet_p, bet_c_over, bet_c_under, bet_e)
        total_bet += a
        correct_bet += b
        correct_bet_ret += c

    n_samples = len(results)
    bet_ratio = total_bet / n_samples
    correct_ratio = correct_bet / total_bet

    print(f"下注: {total_bet}/{n_samples} ({bet_ratio*100:.2f}%)")
    print(f"正确: {correct_bet}/{total_bet} ({correct_ratio*100:.2f}%)")
    print(f"盈亏: {correct_bet_ret/total_bet:.2f} = {correct_bet_ret:.2f}/{total_bet:.2f}")
