#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/4/17
# @Author  : yanxiaodong
# @File    : rle.py
"""
from typing import Dict
import numpy as np


def rle_to_mask(rle: Dict, pixel_index: int = 1):
    """
    Rle to mask.
    """
    rle_count = rle['counts']
    width, height = rle['size'][0], rle['size'][1]

    start = 0
    pixel = 0
    mask = np.zeros(height * width, dtype=np.uint8)
    for num in rle_count:
        stop = start + num
        mask[start:stop] = pixel
        pixel = pixel_index - pixel
        start = stop
    mask = mask.reshape((height, width))

    return mask