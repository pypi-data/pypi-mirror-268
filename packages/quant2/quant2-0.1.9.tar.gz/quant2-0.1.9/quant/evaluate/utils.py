import re
from math import isclose
from quant.football.data.utils import convert_odds_data


def filter_odds_by_time(odds_data, time_range):
    # odds_data = [['77', '1-2', '1.60', '3.5', '0.47', '10-02 00:39', '滚']]
    if len(odds_data) < 1 or len(odds_data[0]) != 7:
        return []

    time_mini, time_maxi = time_range

    pattern = re.compile(r"[0-9]+")

    tmp_time, tmp_odds, tmp_mini = [], [], []
    for row in odds_data:
        time_this = row[0]
        if isinstance(time_this, str) and pattern.fullmatch(time_this):
            time_this = int(time_this)
            if time_this <= time_maxi:
                tmp_time.append(time_this)
                tmp_odds.append(row)
                if time_this <= time_mini:
                    tmp_mini.append(time_this)

    time_mini = max(tmp_mini) if tmp_mini else time_mini

    out = []
    for time_this, row in zip(tmp_time, tmp_odds):
        if time_this >= time_mini:
            out.append(row)

    out = convert_odds_data(out)

    return out


def compute_bet_overunder_ret(score, bet_p, bet_c_over, bet_c_under, bet_e):
    if bet_e == "none":
        return 0, 0, 0

    correct_bet, correct_bet_ret = 0, 0
    if isclose(score, bet_p, rel_tol=1e-3, abs_tol=0.01):
        correct_bet = 1
        correct_bet_ret = 1.0
    elif score > bet_p and bet_e == "over":
        correct_bet = 1
        correct_bet_ret = bet_c_over
    elif score < bet_p and bet_e == "under":
        correct_bet = 1
        correct_bet_ret = bet_c_under

    return 1, correct_bet, correct_bet_ret


def compute_bet_overunder_e(bet_c_over, bet_c_under, conf_gt, conf_lt, conf_thr):
    conf_eq = 1.0 - conf_gt - conf_lt

    ret_over = conf_eq + conf_gt * bet_c_over - conf_lt
    ret_over_conf = conf_eq + conf_gt
    ret_under = conf_eq + conf_lt * bet_c_under - conf_gt
    ret_under_conf = conf_eq + conf_lt

    ret_over_flag = True if ret_over_conf >= conf_thr else False
    ret_under_flag = True if ret_under_conf >= conf_thr else False

    e, ret, ret_conf, ret_proof = "none", 0.0, 0.0, "s0"
    if ret_over_flag and ret_under_flag:
        if ret_over * ret_over_conf >= ret_under * ret_under_conf:
            e, ret, ret_conf, ret_proof = "over", ret_over, ret_over_conf, "s1"
        else:
            e, ret, ret_conf, ret_proof = "under", ret_under, ret_under_conf, "s2"
    else:
        if ret_over_flag:
            e, ret, ret_conf, ret_proof = "over", ret_over, ret_over_conf, "s3"
        elif ret_under_flag:
            e, ret, ret_conf, ret_proof = "under", ret_under, ret_under_conf, "s4"

    return e, ret, ret_conf, ret_proof


def compute_bet_overunder(probs, odds, ret_thr=1.2, ret_conf_thr=0.7):
    # odds = ['77', '1-2', '1.60', '3.5', '0.47', '10-02 00:39', '滚']
    bet_p = float(odds[3])
    bet_c_over = float(odds[2])
    bet_c_under = float(odds[4])

    _id = int(bet_p + 0.01)
    bet_e, bet_ret, bet_ret_conf, bet_ret_proof = "none", 0.0, 0.0, "s0"
    if isclose(bet_p, _id + 0.0, rel_tol=1e-3, abs_tol=0.01):
        conf_gt, conf_lt = sum(probs[_id + 1:]), sum(probs[:_id])

        bet_e, bet_ret, bet_ret_conf, bet_ret_proof = compute_bet_overunder_e(bet_c_over, bet_c_under, conf_gt, conf_lt, ret_conf_thr)
    elif isclose(bet_p, _id + 0.5, rel_tol=1e-3, abs_tol=0.01):
        conf_gt, conf_lt = sum(probs[_id + 1:]), sum(probs[:_id + 1])

        bet_e, bet_ret, bet_ret_conf, bet_ret_proof = compute_bet_overunder_e(bet_c_over, bet_c_under, conf_gt, conf_lt, ret_conf_thr)

    if bet_ret < ret_thr or bet_ret_conf < ret_conf_thr:
        bet_e = "none"

    return bet_p, bet_c_over, bet_c_under, bet_e, bet_ret, bet_ret_conf, bet_ret_proof
