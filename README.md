# 🐍 doit-algorithm-study

> Do it! 자료구조와 함께 배우는 알고리즘 입문 — 파이썬 편  
> 2025.04.09 ~ 07.31 · 주 1회 · 1시간 · 총 17회

---

## 📁 레포 구조

```
python-dsa-study/
├── README.md
├── curriculum.md
└── week01/
│   ├── summary/
│   │   ├── seoyeon.md
│   │   ├── minsu.md
│   │   └── ...
│   └── solve/
│       ├── seoyeon.py
│       ├── minsu.py
│       └── ...
├── week02/
│   └── ...
└── ...
```

---

## 🌿 브랜치 구조

| 브랜치 | 용도 | PR | 리뷰 |
|--------|------|----|------|
| `main` | 최종 결과물 | 필수 | 불필요 |
| `summary/weekNN/이름` | 주차별 요약 | 필수 | 불필요 |
| `solve/weekNN/이름` | 주차별 풀이 | 필수 | **1명 이상 필수** |

### 브랜치 네이밍 규칙

```
summary/week01/seoyeon   ← N주차 요약
solve/week01/seoyeon     ← N주차 풀이
```

> ⚠️ 주차 번호는 항상 2자리로 맞춰주세요. (week1 ❌ → week01 ✅)

---

## 📝 요약 올리는 방법

### 1. main 브랜치 최신화

```bash
git checkout main
git pull origin main
```

### 2. 요약 브랜치 생성

```bash
git checkout -b summary/week01/이름
```

### 3. 파일 작성 후 커밋

```bash
# week01/summary/ 폴더에 이름.md 파일 생성 후
git add week01/summary/이름.md
git commit -m "docs: week01 요약 - 알고리즘 기초"
```

### 4. 브랜치 push

```bash
git push origin summary/week01/이름
```

### 5. PR 생성 후 머지

- GitHub에서 **Pull Request** 생성
- base: `main` ← compare: `summary/week01/이름`
- 리뷰 없이 바로 **Merge** ✅

---

## 💻 풀이 올리는 방법

### 1. main 브랜치 최신화

```bash
git checkout main
git pull origin main
```

### 2. 풀이 브랜치 생성

```bash
git checkout -b solve/week01/이름
```

### 3. 풀이 작성 후 커밋

```bash
# week01/solve/ 폴더에 이름.py 파일 생성 후
git add week01/solve/이름.py
git commit -m "solve: week01 백준 10828 - 스택"
```

### 4. 브랜치 push

```bash
git push origin solve/week01/이름
```

### 5. PR 생성

- GitHub에서 **Pull Request** 생성
- base: `main` ← compare: `solve/week01/이름`
- PR 본문에 아래 내용 포함

```
## 문제
- 링크:
- 챕터:

## 풀이 접근 방식

## 막혔던 부분
```

### 6. 코드 리뷰 후 머지

- 팀원 **1명 이상 리뷰 및 승인** 후 Merge ✅

---

## ✏️ 커밋 메시지 규칙

| prefix | 용도 | 예시 |
|--------|------|------|
| `docs:` | 요약 파일 | `docs: week01 요약 - 알고리즘 기초` |
| `solve:` | 풀이 파일 | `solve: week01 백준 10828 - 스택` |
| `fix:` | 오류 수정 | `fix: week01 풀이 인덱스 오류 수정` |
| `chore:` | 기타 | `chore: README 업데이트` |

---

## 📋 스터디 규칙

### 참여 규칙
- 요약은 모임 **전날까지** `summary/week0N/이름.md` 로 커밋
- 풀이는 PR로 올리고 멤버들이 **코드 리뷰**
- 못 풀었도 시도한 흔적은 **반드시 가져오기**

### 결석 규칙
- 결석은 **48시간 전** Discord `#결석-사전공유` 채널에 공유
- 개인 결석 최대 **3회**

---

## 🔗 링크

- 📅 [전체 커리큘럼](./curriculum.md)
- 💬 Discord 서버 링크
- 📗 [교재 구매 링크](https://product.kyobobook.co.kr/detail/S000001817975)
