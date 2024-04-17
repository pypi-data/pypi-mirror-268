from ._mask import Mask
import dask.array as da
from dask.array import Array
import matplotlib.pyplot as plt
from numpy import ndarray
from typing import List

class BinaryMask(Mask):
    def __init__(self, image: Array, info: dict, channel_names: List[str]) -> None:
        super().__init__(image, info, channel_names)
        assert image.dtype == bool, "image must be a boolean array"

    def get_thumb(self, target_size: int = 512) -> ndarray:
        assert isinstance(target_size, int), "target_size must be an integer"
        assert target_size > 0, "target_size must be greater than 0"
        coarsen_factor = max([s // target_size for s in self.shape])
        if coarsen_factor == 0:
            coarsen_factor = 1
        image = self.image
        image = image.astype('float32')
        thumb = da.coarsen(da.mean, image, {0: coarsen_factor, 1: coarsen_factor}, trim_excess=True)
        return thumb.compute()

    def show_thumb(self, target_size: int = 512) -> None:
        thumb = self.get_thumb(target_size)
        plt.imshow(thumb, cmap='gray')
        plt.axis('off')
        plt.show()