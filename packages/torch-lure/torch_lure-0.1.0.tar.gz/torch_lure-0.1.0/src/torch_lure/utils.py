import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset, Sampler


class RandomSampler(Sampler):
    def __init__(self, dataset, max_steps, batch_size, drop_last=False, seed=None):
        self.dataset = dataset
        self.max_steps = max_steps
        self.batch_size = batch_size
        self.drop_last = drop_last
        self.seed = seed

    def __iter__(self):
        if self.seed:
            np.random.set_state(self.seed)
        indices = np.arange(len(self.dataset))
        np.random.shuffle(indices)

        batches = [
            indices[i : i + self.batch_size]
            for i in range(0, len(indices), self.batch_size)
        ]
        batches = batches[: self.max_steps]

        if not self.drop_last:
            remaining_batches = batches[self.max_steps :]
            if remaining_batches:
                remaining_indices = np.concatenate(remaining_batches, axis=0)
                if len(remaining_indices) > 0:
                    batches.append(remaining_indices)

        return iter(batches)

    def __len__(self):
        if self.drop_last:
            return min(len(self.dataset) // self.batch_size, self.max_steps)
        else:
            return self.max_steps


def random_dataloader(dataset: Dataset, max_steps: int, batch_size: int):
    sampler = RandomSampler(dataset, max_steps=max_steps, batch_size=batch_size)
    dataloader = DataLoader(dataset, batch_size=None, sampler=sampler)
    return dataloader
