# Trademark Search Web App

## 📌 소개

이 프로젝트는 상표(trademark) 데이터를 기반으로 **제품명 검색** 및 **등록 상태 필터링** 기능을 제공하는 웹 애플리케이션입니다. 검색 자동완성, 동적 필터링, 페이지네이션 기능 등을 포함하고 있어 빠르고 편리하게 원하는 정보를 조회할 수 있습니다.

---

## 🚀 실행 방법

### 1. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
uvicorn main:app --reload
```

### 3. 접속

```
http://localhost:8000
```

## 🔧 구현된 기능 설명

* **자동완성(Auto-complete)**

  * 제품명을 입력할 때, 연관된 이름을 실시간으로 제안합니다.

* **동적 등록 상태 필터링**

  * 제품명을 입력하면 해당 제품명과 일치하는 상표 등록 상태 옵션이 필터링되어 표시됩니다.

* **결과 테이블 정렬 및 페이지네이션**

  * 검색 결과는 테이블 형태로 표시되며, 10개 단위로 페이지를 넘기며 확인할 수 있습니다.

---

## 💡 기술적 의사결정에 대한 설명

* **자동완성 기능 구현 방식**

  * 클라이언트에서 input 이벤트를 감지해 /autocomplete API를 호출하는 방식으로 구성해, 부드러운 UX를 제공.

* **페이지네이션 구현**

  * 한 번에 모든 데이터를 로드하면 너무 방대한 데이터라, 10개씩 보여주는 방식으로 사용자 경험과 성능을 모두 고려.

* **FastAPI 엔드포인트 설계**

  * /autocomplete 라우트를 FastAPI로 구현하여, 클라이언트에서 전달받은 query 문자열을 기준으로 productName 컬럼에서 해당 문자열을 포함하는 항목들을 필터링하여 반환.
---

## 🤔 문제 해결 과정에서 고민했던 점

* 여러 편의 기능을 추가하면서 본래 과제의 방향성과 어긋나는 것은 아닌지 고민함

## 🔧 개선하고 싶은 부분 (선택사항)

 * ✅ 테이블의 크기를 조정하여 정보를 한눈에 확인할 수 있도록 개선
