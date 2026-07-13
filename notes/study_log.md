# 학습 일지

## 2026-07-13 (월) · Track 1 Deep-ML · Linear Algebra easy 27 (기저 변환)
**진행**: Problem 27(Transformation Matrix from Basis B to C) 완료. 풀이 `01_deep_ml/p027_transformation_matrix_B_to_C.py` = `np.round(np.linalg.inv(C) @ B, 4).tolist()`. 채점 case1 PASS, case2는 Deep-ML 원본 정답 문자열의 군더더기 공백(`0.125 ]`) 때문에 FAIL로 뜨나 숫자 완전 동일 → 실질 정답. 이번 세션은 코드보다 **개념 이해에 집중**(사용자가 기저 변환 개념 자체를 처음부터 다시 잡음).

**다음 세션 시작점**: **Problem 35 (Convert Vector to Diagonal Matrix)** — `python tools/dml.py show 35` → 풀이 입력 → `grade 35`. 1D 벡터를 대각행렬로. 힌트: numpy에 제목과 거의 같은 이름의 전용 함수 있음. ⚠️ 이 문제 출력 예시는 numpy 스타일(콤마 없음)이라 27번과 달리 `.tolist()` 없이 ndarray째 반환이 맞을 가능성 — 채점으로 확인. Linear Algebra easy 순서: 1~5·27 완료 → 35 → 65 → 66 → 67 → 76 → 83 → 84.

**배운 것 3줄 (개념)**
1. "B→C 변환"은 기저행렬 B를 C로 바꾸는 게 아니라 **같은 벡터의 좌표 표기를 B식→C식으로 다시 쓰는 것**. 변환 대상은 좌표벡터 v_B이지 행렬 B가 아님 (인치→cm 단위변환 비유: 자가 아니라 측정값이 바뀜)
2. **기저행렬 × 좌표 = 표준좌표** (`C·v_C = 표준`). 이유: 행렬곱 `C·[a,b]`는 C의 열(기저벡터)들을 좌표만큼 섞는 것 = `a·c₁+b·c₂`인데 이게 좌표의 정의 그 자체
3. 두 식 `C·v_C = B·v_B`에 `v_C=P·v_B` 대입 → **C·P=B → P=C⁻¹·B**. 순서 중요: `C·P·v_B`는 오른쪽(안)부터 적용(P가 B→C좌표, 그 다음 C가 C좌표→표준). `B·P=C`, `P·B=C` 둘 다 틀림(수치 검증 False). B=단위행렬이면 P=C⁻¹

**반복 실수 패턴 (교정 대상)**: 없음(이번엔 개념 세션). numpy 함수는 array-like(리스트) 입력 OK지만 **출력은 ndarray** → 채점이 print 비교인 문제에선 여전히 `.tolist()` 필요함을 재확인.

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
