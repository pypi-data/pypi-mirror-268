import torch
import torch.utils.data
from pathlib import Path
from quant.utils.io import load_json, load_pkl


def get_dataset(dataset_type, *args, **kwargs):
    if dataset_type == "ClassificationDataset":
        return ClassificationDataset(*args, **kwargs)
    elif dataset_type == "FootballDatasetV1":
        return FootballDatasetV1(*args, **kwargs)
    elif dataset_type == "FootballDatasetV2":
        return FootballDatasetV2(*args, **kwargs)
    else:
        raise NotImplementedError(f"Not supported <{dataset_type=}>.")


class ClassificationDataset(torch.utils.data.Dataset):

    def __init__(self, data_file):
        self.X, self.Y = self._load_data(data_file)

    def _load_data(self, data_file):
        # data_file: list[tuple[list,int]]
        X, Y = [], []

        suffix = Path(data_file).suffix
        if suffix == ".json":
            _X, _Y = load_json(data_file)[:2]
        elif suffix == ".pkl":
            _X, _Y = load_pkl(data_file)[:2]
        else:
            raise NotImplementedError(f"Not supported <{suffix=}>.")

        for x, y in zip(_X, _Y):
            X.append(torch.tensor(x, dtype=torch.float))
            Y.append(y)

        return X, Y

    def __getitem__(self, index):
        x, y = self.X[index], self.Y[index]
        return x, y

    def __len__(self):
        return len(self.X)


class FootballDatasetV1(torch.utils.data.Dataset):

    def __init__(self, data_file):
        self.X, self.Y = self._load_data(data_file)

    def _load_data(self, data_file):
        # data_file: list[tuple[list,int]]
        X, Y = [], []

        suffix = Path(data_file).suffix
        if suffix == ".json":
            _X, _Y = load_json(data_file)[:2]
        elif suffix == ".pkl":
            _X, _Y = load_pkl(data_file)[:2]
        else:
            raise NotImplementedError(f"Not supported <{suffix=}>.")

        for x, y in zip(_X, _Y):
            # x_home, x_away, x_features = x[0], x[1], x[2:]
            X.append((x[0], x[1], torch.tensor(x[2:], dtype=torch.float)))
            Y.append(y)

        return X, Y

    def __getitem__(self, index):
        x, y = self.X[index], self.Y[index]
        return x, y

    def __len__(self):
        return len(self.X)


class FootballDatasetV2(torch.utils.data.Dataset):

    def __init__(self, data_file):
        self.X, self.Y = self._load_data(data_file)

    def _load_data(self, data_file):
        # data_file: list[tuple[list,int]]
        X, Y = [], []

        suffix = Path(data_file).suffix
        if suffix == ".json":
            _X, _Y = load_json(data_file)[:2]
        elif suffix == ".pkl":
            _X, _Y = load_pkl(data_file)[:2]
        else:
            raise NotImplementedError(f"Not supported <{suffix=}>.")

        for x, y in zip(_X, _Y):
            # x_season, x_home, x_away, x_features = x[0], x[1], x[2], x[3:]
            X.append((x[0], x[1], x[2], torch.tensor(x[3:], dtype=torch.float)))
            Y.append(y)

        return X, Y

    def __getitem__(self, index):
        x, y = self.X[index], self.Y[index]
        return x, y

    def __len__(self):
        return len(self.X)


class RegressionDataset(torch.utils.data.Dataset):

    def __init__(self, data_file):
        self.X, self.Y = self._load_data(data_file)

    def _load_data(self, data_file):
        # data_file: list[tuple[list,list]]
        X, Y = [], []

        suffix = Path(data_file).suffix
        if suffix == ".json":
            _X, _Y = load_json(data_file)[:2]
        elif suffix == ".pkl":
            _X, _Y = load_pkl(data_file)[:2]
        else:
            raise NotImplementedError(f"Not supported <{suffix=}>.")

        for x, y in zip(_X, _Y):
            X.append(torch.tensor(x, dtype=torch.float))
            Y.append(torch.tensor(y, dtype=torch.float))

        return X, Y

    def __getitem__(self, index):
        x, y = self.X[index], self.Y[index]
        return x, y

    def __len__(self):
        return len(self.X)


class MultiBranchDataset(torch.utils.data.Dataset):

    def __init__(self, data_file):
        self.X, self.Y = self._load_data(data_file)

    def _load_data(self, data_file):
        raise NotImplementedError("TODO")

    def __getitem__(self, index):
        x, y = self.X[index], self.Y[index]
        return x, y

    def __len__(self):
        return len(self.X)
