# Problem 2: Transpose of a Matrix
# https://www.deep-ml.com/problems/2 · Linear Algebra · easy
# 풀이일: 2026-07-08 · 로컬 채점 2/2 통과
# 포인트: 결과는 J×I로 사전할당, [[0]*I]*J는 행 공유 함정 → 컴프리헨션 사용


def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    I = len(a)
    J = len(a[0])
    k = [[0] * I for _ in range(J)]
    for i in range(I):
        for j in range(J):
            k[j][i] = a[i][j]
    return k
