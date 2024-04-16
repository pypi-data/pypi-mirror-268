import quant
from pathlib import Path
from quant.football.data.utils import train_test
from quant.football.transforms import table20240414 as table_factory
from quant.utils.io import load_pkl, make_dir, save_json, save_pkl
print(f"{quant.__version__=}")


def make_datasets(file, date_min, date_sep, date_max, name_suffix, points, *preprocess_args):
    # 加载数据
    dataset = load_pkl(file)
    print(f"[1] {len(dataset)=}, {len(dataset[0])=}")

    # 检测得分数据是否对齐
    good_data, bad_data, bad_info = table_factory.check_samples(dataset)
    print(f"[2] {len(good_data)=}, {len(bad_data)=}, {bad_info[:3]}")

    # 拆分训练与测试数据子集
    train_data, test_data = train_test(good_data, date_sep, date_min, date_max)
    print(f"[3] {len(train_data)=}, {len(test_data)=}")

    # 忽略比赛不足`n`场的球队比赛
    train_data = table_factory.filter_samples(train_data, limit=6)
    print(f"[4] {len(train_data)=}")

    # 准备数据目录
    out_dir = Path(file).parent.as_posix() + name_suffix
    out_dir = make_dir(out_dir, exist_ok=False)

    # 转换并导出训练数据集(按需计算预处理参数)
    if points is None:
        X, Y, Z, *preprocess_args = table_factory.export_dataset(train_data, *preprocess_args)
    else:
        X, Y, Z, *preprocess_args = table_factory.export_dataset(train_data, points, *preprocess_args)
    print(f"[Train] save {len(X)} rows, {len(X[0])} cols")
    save_pkl(out_dir / "train.pkl", [X, Y, Z])

    # 转换并导出测试数据集(使用训练数据集的预处理参数)
    if points is None:
        X, Y, Z, *preprocess_args = table_factory.export_dataset(test_data, *preprocess_args)
    else:
        X, Y, Z, *preprocess_args = table_factory.export_dataset(test_data, points, *preprocess_args)
    print(f"[Test] save {len(X)} rows, {len(X[0])} cols")
    save_pkl(out_dir / "test.pkl", [X, Y, Z])

    # 打印编码器嵌入字典的大小
    encoder = preprocess_args[1]
    print(f"[Embedding] season {encoder['season']['__len__']}, team {encoder['team']['__len__']}")

    # 保存预处理参数
    save_json(out_dir / "preprocess.json", preprocess_args)

    return out_dir


# 转换特征+拆分数据集+导出数据到文件
file = "path_of_samples_file"

date_min = "2023-01-01"
date_sep = "2024-01-01"
date_max = "2024-04-01"

name_suffix = "_train_2301_2312_2403_s5_label_whole_c15_maxabs_direct"

points = [i + 0.5 for i in range(15, 90)]
points = None

preprocess_args = [5, "label", True, 15, "maxabs", "direct"]

make_datasets(file, date_min, date_sep, date_max, name_suffix, points, *preprocess_args)
