import numpy as np


def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    # P = C^-1 · B  (B가 단위행렬이면 결과는 C^-1)
    return np.round(np.linalg.inv(C) @ B, 4).tolist()
