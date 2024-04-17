from ..image._ubyte_image import UByteImage
import dask.array as da
import json
import os
from typing import List

def read_zarr_img(zarr_path: str, meta_path: str, channel_names: List[str] = None) -> UByteImage:
    assert isinstance(zarr_path, str)
    assert zarr_path.endswith('.zarr')
    assert os.path.exists(zarr_path)
    assert isinstance(meta_path, str)
    assert meta_path.endswith('.json')
    assert os.path.exists(meta_path)
    img = da.from_zarr(zarr_path)
    with open(meta_path, 'r') as f:
        meta = json.load(f)
    if channel_names is None:
        if 'channel_names' in meta:
            channel_names = meta['channel_names']
        else:
            channel_names = ['Red', 'Green', 'Blue']
    if str(img.dtype) == "uint8":
        return UByteImage(img, meta, channel_names)
    else:
        raise NotImplementedError(f"Images of type {str(img.dtype)} are not supported yet.")