# Problem 3: Reshape Matrix
# https://www.deep-ml.com/problems/3 · Linear Algebra · easy
# 풀이일: 2026-07-08 · 로컬 채점 4/4 통과
# 포인트: reshape는 in-place 아님(새 배열 반환), np.array→reshape→tolist 체인

import numpy as np


def reshape_matrix(a: list[list[int | float]], new_shape: tuple[int, int]) -> list[list[int | float]]:
    if new_shape[0] * new_shape[1] != len(a) * len(a[0]):
        return []
    else:
        a = np.array(a).reshape(new_shape)
        a = a.tolist()
        return a
