import copy
from quant.utils.io import load_json


cfg = dict(
    data=dict(
        type="FootballDatasetV1",
        data_root="/datasets/table20240326_2001to2306_train_2001_2305_s5_label_whole_c15_maxabs",
        train_file="train.pkl",
        test_file="test.pkl",
        batch_size=128),
    model=dict(
        type="STNetV3",
        in_features=98,
        hidden_features=192,
        out_features=15,
        n_layers=1,
        bias=True,
        drop=0.2,
        enable_skip=False),
    loss=dict(type="CrossEntropyLoss", reduction="mean"),
    optimizer=dict(
        type="SGD",
        lr=0.2,
        weight_decay=0.0001),
    scheduler=dict(
        type="StepLR",
        step_size=10,
        gamma=0.1),
    runtime=dict(
        seed=1,
        epochs=30,
        device="cuda",
        log_interval=50))


def get_config(config_file=None):
    if config_file:
        _cfg = load_json(config_file)
    else:
        _cfg = copy.deepcopy(cfg)
    return _cfg


def merge_from_str(cfg, args):
    # terminal: model.backbone.depth=50
    # terminal: model.backbone.type='"resnet"'
    # terminal: model.backbone.out_indices='(0, 1, 2, 3)'
    cfg = copy.deepcopy(cfg)
    for arg in args:
        key, val = arg.split("=", maxsplit=1)

        d = cfg
        sub_keys = key.split(".")
        for sub_key in sub_keys[:-1]:
            d.setdefault(sub_key, dict())
            d = d[sub_key]

        sub_key = sub_keys[-1]
        d[sub_key] = eval(val)
    return cfg


def merge_from_dict(cfg, options):
    # dict: {"model.backbone.out_indices": (0, 1, 2, 3)}
    cfg = copy.deepcopy(cfg)
    for key, val in options.items():
        d = cfg
        sub_keys = key.split(".")
        for sub_key in sub_keys[:-1]:
            d.setdefault(sub_key, dict())
            d = d[sub_key]

        sub_key = sub_keys[-1]
        d[sub_key] = val
    return cfg
