# 학습 일지

<!--
템플릿 (매 세션 종료 시 맨 위에 추가):

## YYYY-MM-DD (요일) · Track N · 주제
**진행**: 무엇을 풀었는지 (파일 경로 포함)
**다음 세션 시작점**: 정확한 문제 번호/단계
**배운 것 3줄**
**반복 실수 패턴 (교정 대상)**
-->

## 2026-07-08 (수) · 셋업
**진행**: 프로젝트 스캐폴딩 완료. 폴더 구조 생성, srush 퍼즐 5종 + CS336 assignment1 클론(`_external/`), GitHub repo 생성·푸시.

**다음 세션 시작점**: **Track 1 Deep-ML, Problem 1 (Matrix-Vector Dot Product)** — https://www.deep-ml.com/problems/1 부터 Linear Algebra 카테고리 easy 순서대로.

**세션 운영 방식**: 사용자가 채팅에 풀이 코드 입력 → Claude가 실행·테스트 검증 → 정답이면 `01_deep_ml/pNNN_문제명.py`로 저장 → 세션 끝에 이 파일 + PROGRESS.md 갱신 후 commit & push. Claude는 대신 풀지 않고 오답 시 단계별 힌트만.

**환경 메모**: GPU 없음. GPU Puzzles는 `NUMBA_ENABLE_CUDASIM=1`, CS336 Triton 과제는 Colab.
