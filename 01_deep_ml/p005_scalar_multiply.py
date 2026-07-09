# Problem 5: Scalar Multiplication of a Matrix
# https://www.deep-ml.com/problems/5 · Linear Algebra · easy
# 풀이일: 2026-07-09 · 로컬 채점 2/2 통과 (시도 4회)
# 포인트: .메서드가 *보다 먼저 붙음 → (배열 곱셈식).tolist() 괄호 필수.
#         파이썬 리스트 * 정수 = 반복([1,2]*2=[1,2,1,2]), 원소별 곱은 numpy 배열에서만.

import numpy as np


def scalar_multiply(matrix: list[list[int | float]], scalar: int | float) -> list[list[int | float]]:
    return (np.array(matrix) * scalar).tolist()
