# Problem 1: Matrix-Vector Dot Product
# https://www.deep-ml.com/problems/1 · Linear Algebra · easy
# 풀이일: 2026-07-08 · 로컬 채점 3/3 통과


def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    result = []
    if len(a[0]) != len(b):
        return -1
    for a_ in a:
        inner_result = 0
        for i, element in enumerate(a_):
            inner_result += element * b[i]
        result.append(inner_result)
    return result
