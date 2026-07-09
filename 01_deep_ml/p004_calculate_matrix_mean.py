# Problem 4: Calculate Mean by Row or Column
# https://www.deep-ml.com/problems/4 · Linear Algebra · easy
# 풀이일: 2026-07-09 · 로컬 채점 2/2 통과
# 포인트: column 평균=행 방향 축소=axis=0, row 평균=axis=1. numpy 반환은 반드시 tolist()

import numpy as np


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    M = np.array(matrix)
    mode = 0 if mode == 'column' else 1
    return M.mean(axis=mode).tolist()
