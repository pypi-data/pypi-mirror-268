import copy
import pathlib
from quant.football.data.utils import time_str2secs
from quant.utils.io import load_pkl, save_pkl


def split_datasets(datasets, date_min, date_sep, date_max):
    datasets = copy.deepcopy(datasets)

    X, Y, Z = [], [], []
    for _X, _Y, _Z in datasets:
        X, Y, Z = X + _X,  Y + _Y, Z + _Z

    date_min = time_str2secs(date_min)
    date_sep = time_str2secs(date_sep)
    date_max = time_str2secs(date_max)

    train_X, train_Y, train_Z = [], [], []
    test_X, test_Y, test_Z = [], [], []
    # z: 比赛ID,比赛时间,比赛状态,...
    for x, y, z in zip(X, Y, Z):
        ts = z[1]  # match_time
        if ts < date_min:
            continue
        elif ts < date_sep:
            train_X.append(x)
            train_Y.append(y)
            train_Z.append(z)
        elif ts < date_max:
            test_X.append(x)
            test_Y.append(y)
            test_Z.append(z)

    subset_train = [train_X, train_Y, train_Z]
    subset_test = [test_X, test_Y, test_Z]
    return subset_train, subset_test


# 根据开赛时间拆分数据子集对
data_root = pathlib.Path("path_of_dataset_root_dir")
train_data = load_pkl(data_root / "train.pkl")
test_data = load_pkl(data_root / "test.pkl")

date_min = "2024-01-01"
date_sep = "2024-02-01"
date_max = "2024-04-01"

subset_train, subset_test = split_datasets([train_data, test_data], date_min, date_sep, date_max)
save_pkl(data_root / "split_2401_2401.pkl", subset_train)
save_pkl(data_root / "split_2402_2403.pkl", subset_test)
print(f"{len(subset_train[0])}+{len(subset_test[0])}")
