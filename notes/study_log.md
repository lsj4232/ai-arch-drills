# 학습 일지

## 2026-07-09 (목) · Track 1 Deep-ML · Linear Algebra easy 4~5
**진행**: Problem 4(Mean by Row/Column, 2/2) · 5(Scalar Multiplication, 2/2, 시도 4회) 완료. 풀이는 `01_deep_ml/p004~p005_*.py`.

**다음 세션 시작점**: **Problem 27 (Transformation Matrix from Basis B to C)** — `python tools/dml.py show 27` → 풀이 입력 → `grade 27`. 문제는 이미 제시받은 상태였음. 개념 힌트 받음: B좌표→표준좌표는 B 곱, 표준→C좌표는 C 역행렬(`np.linalg.inv`) 곱, 행렬곱은 `@`, 출력은 소수 4자리 반올림(`np.round(...,4)`). Linear Algebra easy 5/15 완료, 이후 35 → 65 → ... 순.

**배운 것 3줄**
1. numpy 계산 결과 반환은 무조건 `.tolist()` — 채점이 print 문자열 비교라 numpy 스타일 `[4. 5. 6.]`은 무조건 탈락
2. 메서드 호출(`.`)이 산술연산자보다 우선 결합 → `(np.array(m)*s).tolist()`처럼 식 전체를 괄호로 감싸고 붙일 것
3. 파이썬 리스트 `* 정수`는 원소별 곱이 아니라 **반복**(`[1,2]*2=[1,2,1,2]`, `*-1`은 빈 리스트) — 원소별 연산은 numpy 배열 상태에서만

**반복 실수 패턴 (교정 대상)**: `.tolist()` 누락이 p004에서 지적받고 p005에서 재발(누적 2회) — "numpy 반환 직전 tolist" 반사화 필요. 연산자 우선순위로 tolist 위치 오류 2회.

## 2026-07-08 (수) · Track 1 Deep-ML · Linear Algebra easy 1~3
**진행**: Problem 1(Matrix-Vector Dot Product, 3/3) · 2(Transpose, 2/2) · 3(Reshape, 4/4) 완료 — 오늘 목표 3문제 달성. 풀이는 `01_deep_ml/p001~p003_*.py`.

**다음 세션 시작점**: **Problem 4 (Calculate Mean by Row or Column)** — `python tools/dml.py show 4` → 풀이 입력 → `grade 4`. Linear Algebra easy 순서 계속 (완료 3/15).

**페이스 기준**: easy 하루 3~5문제, medium부터 1~3문제. 20분 막히면 힌트 요청.

**배운 것 3줄**
1. 내적은 "곱하고 끝"이 아니라 행 단위 누적합 — 누적자 변수를 행마다 0으로 리셋 후 행당 1개 append
2. 2차원 사전할당은 `[[0]*n]*m` 금지(행이 같은 객체 공유) → `[[0]*n for _ in range(m)]`; 전치 결과 크기는 J×I로 뒤집기
3. numpy reshape는 in-place가 아니라 새 배열 반환, 리스트에는 reshape 없음 → `np.array(a).reshape(...).tolist()`; 채점이 print 비교라 반환은 반드시 tolist()

**반복 실수 패턴 (교정 대상)**: `return` 문 누락 2회(p002, p003 초안) — 함수는 마지막에 반환까지가 완성. `np.array`를 `a.array`로 오타 1회 (모듈 함수 vs 객체 메서드 구분).

템플릿 (매 세션 종료 시 맨 위에 추가):

## YYYY-MM-DD (요일) · Track N · 주제
**진행**: 무엇을 풀었는지 (파일 경로 포함)
**다음 세션 시작점**: 정확한 문제 번호/단계
**배운 것 3줄**
**반복 실수 패턴 (교정 대상)**
-->

## 2026-07-08 (수) · 셋업
**진행**: 프로젝트 스캐폴딩 완료. 폴더 구조 생성, srush 퍼즐 5종 + CS336 assignment1 + DML-OpenProblem(Deep-ML 문제 원본 165개) 클론(`_external/`), GitHub repo 생성·푸시. 로컬 채점기 `tools/dml.py` 작성, 공식 solution으로 3/3 통과 검증. Tensor Puzzles 하네스(`lib.py` make_test/run_test)도 로컬 실행 확인 (풀이 함수에 torchtyping 시그니처 필수).

**다음 세션 시작점**: **Track 1 Deep-ML, Problem 2 (Transpose of a Matrix)** — Problem 1은 2026-07-08 완료(3/3). `python tools/dml.py show 2`로 문제 표시 → 사용자 풀이 입력 → `grade 2`로 채점. 이후 Linear Algebra 카테고리 easy 순서대로 (`python tools/dml.py list "Linear Algebra"` 참고).

**세션 운영 방식**: 사용자가 채팅에 풀이 코드 입력 → Claude가 실행·테스트 검증 → 정답이면 `01_deep_ml/pNNN_문제명.py`로 저장 → 세션 끝에 이 파일 + PROGRESS.md 갱신 후 commit & push. Claude는 대신 풀지 않고 오답 시 단계별 힌트만.

**환경 메모**: GPU 없음. GPU Puzzles는 `NUMBA_ENABLE_CUDASIM=1`, CS336 Triton 과제는 Colab.
