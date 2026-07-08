# ai-arch-drills

AI 아키텍처를 바닥부터 구현하며 검증하는 학습 기록. LeetCode처럼 문제 단위로 풀고, 풀이와 진행 이력을 이 repo에 누적한다.

원본 정리 문서: `Desktop/AI_아키텍처_구현_문제셋_정리.docx` (2026-07-06)

## 로드맵 (3트랙, 순차 진행)

### Track 1 — Deep-ML (워밍업, 문제 단위 반복)
- 플랫폼: https://www.deep-ml.com (온라인 채점)
- numpy만으로 attention, layernorm, backprop, optimizer 등 구현
- Linear Algebra → Deep Learning → LLM 카테고리 순
- 풀이 저장: `01_deep_ml/pNNN_문제명.py` (헤더에 문제 링크·카테고리·난이도)

### Track 2 — srush 퍼즐 시리즈 (아키텍처 이해 검증)
| 순서 | 퍼즐 | 폴더 | 내용 |
|---|---|---|---|
| 1 | [Tensor Puzzles](https://github.com/srush/Tensor-Puzzles) | `02_tensor_puzzles/` | broadcasting만으로 21개 연산 |
| 2 | [GPU Puzzles](https://github.com/srush/GPU-Puzzles) | `03_gpu_puzzles/` | numba CUDA 커널 14문제 |
| 3 | [Autodiff Puzzles](https://github.com/srush/Autodiff-Puzzles) | `04_autodiff_puzzles/` | 자동미분 |
| 4 | [Transformer Puzzles](https://github.com/srush/Transformer-Puzzles) | `05_transformer_puzzles/` | transformer 내부 동작 |
| 5 | [LLM Training Puzzles](https://github.com/srush/LLM-Training-Puzzles) | `06_llm_training_puzzles/` | 분산학습(FSDP 개념) |

### Track 3 — Stanford CS336: Language Modeling from Scratch
- https://github.com/stanford-cs336 — BPE 토크나이저 → transformer → flash attention(Triton) → 분산학습 → RLHF
- pytest 테스트로 채점. 풀이: `07_cs336/assignmentN/`

### 예비 트랙 (Track 3 이후 선택)
LeetGPU(브라우저 CUDA 채점) · KernelBench · CMU 10-414(needle) · minitorch · ARENA

## 환경 제약
- 로컬: Python 3.12, numpy, torch CPU 전용. **GPU 없음.**
- GPU Puzzles → `NUMBA_ENABLE_CUDASIM=1` 시뮬레이터로 로컬 진행
- LeetGPU → 브라우저 채점 (GPU 불필요)
- CS336 Triton/분산 과제 → Colab 병행

## 운영 방식 (Claude Code 세션)
1. 세션 시작: `notes/study_log.md`의 **"다음 세션 시작점"** 확인 — 진행 위치의 단일 진실
2. 문제 제시 → 사용자가 채팅에 풀이 입력 → Claude가 실행·테스트 검증 (Claude가 대신 풀지 않음)
3. 오답이면 단계별 힌트, 정답이면 트랙 폴더에 파일 저장
4. 세션 종료: study_log.md(배운 것·실수 패턴·다음 시작점) + PROGRESS.md 갱신 → commit & push

## 저작권 원칙
문제 원문은 repo에 복사하지 않고 링크만. 커밋 대상은 내 풀이 코드와 진행 기록만. 원본 repo 클론은 `_external/`(gitignore)에 둔다.
