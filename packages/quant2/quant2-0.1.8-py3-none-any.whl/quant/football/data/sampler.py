import numpy as np
from torch.utils.data import Sampler
from typing import Iterator, Optional


class RandomSubsetSampler(Sampler[int]):

    def __init__(self, data_size: int, num_samples: Optional[int] = None, fraction: Optional[float] = None) -> None:
        """
        初始化 RandomSubsetSampler。

        参数:
        - data_size (int): 数据集中的样本总数。
        - num_samples (Optional[int]): 每个 epoch 的样本数量。
        - fraction (Optional[float]): 每个 epoch 采样的数据比例。
        """
        if num_samples is None:
            fraction = fraction if fraction is not None else 0.2
            num_samples = int(np.ceil(data_size * fraction))

        self.data_size = data_size
        self.num_samples = num_samples

    def __iter__(self) -> Iterator[int]:
        indices = np.random.choice(self.data_size, self.num_samples, replace=False)
        return iter(indices)

    def __len__(self) -> int:
        return self.num_samples
