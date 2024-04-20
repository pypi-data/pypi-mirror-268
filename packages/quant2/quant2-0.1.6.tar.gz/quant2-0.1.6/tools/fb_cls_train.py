# PYTHONPATH=$(pwd) python tools/fb_cls_train.py
import numpy as np
import random
import sys
import time
import torch
from copy import deepcopy
from pathlib import Path
from quant.football.data.dataset import get_dataset
from quant.football.data.sampler import RandomSubsetSampler
from quant.football.models import get_model
from quant.utils.config import get_config, merge_from_dict
from quant.utils.io import copy_file, save_json
from quant.utils.logging import get_logger, print_log


def train(model, device, train_loader, loss_fn, optimizer, epoch, log_interval, verbose, logger):
    model.train()
    dataloader_size = len(train_loader)
    for batch_idx, (data, target) in enumerate(train_loader, 1):
        data = [e.to(device) for e in data] if isinstance(
            data, (list, tuple)) else data.to(device)
        target = [e.to(device) for e in target] if isinstance(
            target, (list, tuple)) else target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print_log(
                f"Train Epoch: {epoch} [{batch_idx}/{dataloader_size}] Loss: {loss.item():.6f}", verbose, logger)


def test(model, device, test_loader, loss_fn, verbose, logger):
    model.eval()
    test_loss, correct = 0, 0
    with torch.no_grad():
        for data, target in test_loader:
            data = [e.to(device) for e in data] if isinstance(
                data, (list, tuple)) else data.to(device)
            target = [e.to(device) for e in target] if isinstance(
                target, (list, tuple)) else target.to(device)
            output = model(data)
            test_loss += loss_fn(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()

    test_loss /= len(test_loader)
    dataset_size = len(test_loader.dataset)
    test_acc = correct / dataset_size

    print_log(
        f"\nTest set: Avg loss: {test_loss:.6f}, Acc: {correct}/{dataset_size} ({test_acc:.4f})\n", verbose, logger)
    return test_acc


def main(cfg, verbose=True):
    _cfg = deepcopy(cfg)
    data_cfg, model_cfg, loss_cfg, optimizer_cfg, scheduler_cfg, runtime_cfg = \
        cfg["data"], cfg["model"], cfg["loss"], cfg["optimizer"], cfg["scheduler"], cfg["runtime"]

    seed = runtime_cfg.get("seed", 1)
    epochs = runtime_cfg.get("epochs", 90)
    device = runtime_cfg.get("device", "cuda")
    log_interval = runtime_cfg.get("log_interval", 10)

    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

    if device == "cuda" and torch.cuda.is_available():
        device = torch.device("cuda")
    else:
        device = torch.device("cpu")

    dataset_type = data_cfg.pop("type")
    data_root = Path(data_cfg["data_root"])
    train_dataset = get_dataset(dataset_type, data_root / data_cfg["train_file"])
    test_dataset = get_dataset(dataset_type, data_root / data_cfg["test_file"])

    fraction = data_cfg.get("fraction", None)
    num_samples = data_cfg.get("num_samples", None)
    sampler = RandomSubsetSampler(len(train_dataset), num_samples, fraction)

    num_workers = data_cfg.get("num_workers", 8)

    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=data_cfg["batch_size"], sampler=sampler, num_workers=num_workers, drop_last=True
    )
    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=128, num_workers=num_workers
    )

    model_type = model_cfg.pop("type")
    model = get_model(model_type, **model_cfg)

    checkpoint = model_cfg.get("checkpoint", None)
    if checkpoint is not None:
        model.load_state_dict(torch.load(checkpoint, map_location=torch.device("cpu")))

    # layers, layers.0, layers.0.1, norm, head.weight, head.bias
    frozen_layers = model_cfg.get("frozen_layers", None)
    if frozen_layers is not None:
        for name, param in model.named_parameters():
            param.requires_grad = True
            for layer_name in frozen_layers:
                if layer_name in name:
                    param.requires_grad = False
                    break

    # season_embedding, team_embedding, stem
    trainable_layers = model_cfg.get("trainable_layers", None)
    if trainable_layers is not None:
        for name, param in model.named_parameters():
            param.requires_grad = False
            for layer_name in trainable_layers:
                if layer_name in name:
                    param.requires_grad = True
                    break

    model = model.to(device)

    loss_type = loss_cfg.pop("type")
    if loss_type == "CrossEntropyLoss":
        from torch.nn import CrossEntropyLoss
        loss_fn = CrossEntropyLoss(**loss_cfg).to(device)
    else:
        raise NotImplementedError(f"Not supported <{loss_type}>.")

    params = [param for param in model.parameters() if param.requires_grad]
    optimizer_type = optimizer_cfg.pop("type")
    if optimizer_type == "SGD":
        from torch.optim import SGD
        optimizer_cfg.setdefault("momentum", 0.9)
        optimizer = SGD(params, **optimizer_cfg)
    elif optimizer_type == "AdamW":
        from torch.optim import AdamW
        optimizer_cfg.setdefault("betas", (0.9, 0.999))
        if isinstance(optimizer_cfg["betas"], str):
            optimizer_cfg["betas"] = eval(optimizer_cfg["betas"])
        optimizer = AdamW(params, **optimizer_cfg)
    else:
        raise NotImplementedError(f"Not supported <{optimizer_type}>.")

    scheduler_type = scheduler_cfg.pop("type")
    if scheduler_type == "StepLR":
        from torch.optim.lr_scheduler import StepLR
        scheduler = StepLR(optimizer, **scheduler_cfg)
    else:
        raise NotImplementedError(f"Not supported <{scheduler_type}>.")

    trial_name = time.strftime("%Y%m%d%H%M%S")
    out_dir = Path("runs") / data_root.name / trial_name
    out_dir.mkdir(parents=True, exist_ok=True)
    copy_file(data_root, out_dir, "*.json")

    logger = get_logger(__name__, False, out_dir / "log.txt")

    best_acc, best_epoch = 0.0, -1
    for epoch in range(1, epochs + 1):
        train(model, device, train_loader, loss_fn, optimizer,
              epoch, log_interval, verbose, logger)
        curr_acc = test(model, device, test_loader, loss_fn,
                        verbose, logger)
        if curr_acc > best_acc:
            best_acc, best_epoch = curr_acc, epoch
            torch.save(model.state_dict(), out_dir / "best.pt")
        scheduler.step()
    torch.save(model.state_dict(), out_dir / "last.pt")
    last_acc_test = curr_acc

    print_log("[best model]", verbose, logger)
    print_log(f"\noutput dir: {out_dir}", verbose, logger)
    print_log(f"{best_acc=:.4f}, {best_epoch=:03d}\n", verbose, logger)

    print_log("[check train dataset]", verbose, logger)
    check_loader = torch.utils.data.DataLoader(train_dataset, batch_size=128, num_workers=num_workers)
    last_acc_train = test(model, device, check_loader, loss_fn,
                          verbose, logger)

    _cfg["log"] = {
        "out_dir": str(out_dir),
        "date": time.strftime("%Y-%m-%d %H:%M:%S"),
        "best_acc": best_acc,
        "best_epoch": best_epoch,
        "last_acc_test": last_acc_test,
        "last_acc_train": last_acc_train,
    }
    save_json(out_dir / "model.json", _cfg, indent=4)

    return best_acc, _cfg


if __name__ == "__main__":
    options = {}
    for arg in sys.argv[1:]:
        key, val = arg.split("=", maxsplit=1)
        options[key] = eval(val)

    cfg = get_config(options.get("config", None))
    cfg = merge_from_dict(cfg, options)

    best_acc, _cfg = main(cfg, verbose=False)
    print({"default": best_acc, "log": _cfg["log"]})
