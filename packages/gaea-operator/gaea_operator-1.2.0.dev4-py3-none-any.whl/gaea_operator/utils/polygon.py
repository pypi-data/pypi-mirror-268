#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
# @Time    : 2024/4/17
# @Author  : yanxiaodong
# @File    : poly.py
"""
from typing import List
import numpy as np
import cv2


def polygon_to_mask(polygon: List, mask: np.ndarray, pixel_index: int = 1):
    """
    Poly to mask.
    """
    polygon = np.array(polygon)
    size = polygon.size
    assert size % 2 == 0, "polygon size error: {}".format(size)

    polygon = np.array([[polygon[i], polygon[i + 1]] for i in range(size) if i % 2 == 0], dtype=np.int32)
    cv2.fillPoly(mask, [polygon], pixel_index)