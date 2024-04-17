import torch

from ..corruptions import add_randomization


@add_randomization("partial_labels")
def partial_labels(img, target, corruption_prob, get_random_label):
    """
    Randomizes the labels of the dataset.

    Args:
        img (torch.Tensor): Image tensor
        target (torch.Tensor): Target tensor
        corruption_prob (float): Probability of corruption
        get_random_label (callable): Function that returns a random label
        apply_corruption (bool): If True, the corruption is applied to the returned image
    """
    random_label = target
    corrupted = False
    if torch.rand(1) <= corruption_prob:
        corrupted = True
        random_label = get_random_label(target)

        target = random_label

    return img, target, torch.tensor(corrupted, dtype=torch.bool)
