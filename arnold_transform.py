#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import numpy as np

from typing import Literal


TRANSFORM_MATRIX = np.array([
    [2, 1],
    [1, 1]
])

def calculate_transform_number(N: int):
    """
    计算恢复原图需要经过离散猫变换的次数
    Args:
        N (int): 图像的尺寸
    Returns:
        int: 次数
    """
    transform_matrix = TRANSFORM_MATRIX
    n = -1
    while not (transform_matrix == np.eye(2)).all():
        transform_matrix = np.dot(transform_matrix, TRANSFORM_MATRIX) % N
        n += 1
    return n

def arnold_transform(image: np.ndarray, type: Literal['encrypt', 'decrypt']):
    # 判断是否为正方形
    if image.shape[0] != image.shape[1]:
        raise ValueError("image's width and height must be equal")

    N = image.shape[0]

    # 计算离散猫变换的次数
    transform_number = calculate_transform_number(N)
    if type == 'encrypt':
        transform_number = math.ceil(transform_number / 2)
    elif type == 'decrypt':
        transform_number = math.floor(transform_number / 2)
    else:
        raise ValueError("'type' must be one of ['encrypt', 'decrypt']")

    # 计算经过多次变换后最终的变换矩阵
    transform_matrix = TRANSFORM_MATRIX
    for _ in range(transform_number):
        transform_matrix = np.dot(transform_matrix, TRANSFORM_MATRIX) % N

    # 新建一个空的图片
    new_image = np.zeros_like(image)
    for i in range(N):
        for j in range(N):
            new_i = np.dot(np.array([i, j]), transform_matrix[0]) % N
            new_j = np.dot(np.array([i, j]), transform_matrix[1]) % N
            new_image[new_i, new_j] = image[i, j]

    return new_image