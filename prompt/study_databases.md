```
당신은 프로그램 40년차 전문가야.
vs code gemini 에서 사용할  프롬프트를  json 방식으로 만들고, md 파일도 만들어줘,
본인의 의견은 말하지 말고 files 을 만들어줘.

- github repo : study_databases
- 풀이 대상
📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)
아래 요구사항에 맞는 CREATE TABLE 문을 작성하시오.
✔ 요구사항
테이블명: students

컬럼:

id (INT, PRIMARY KEY)

name (VARCHAR(50))

age (INT)

📌 문제 2 — CREATE (INSERT) 기초
✔ 요구사항
위 students 테이블에 다음 데이터를 INSERT 하시오.
id
name
age
1
홍길동
23
2
이영희
21
3
박철수
26
📌 문제 3 — READ (SELECT) 기본 조회
다음 조건들을 만족하는 SELECT 쿼리를 작성하시오.
students 테이블의 전체 데이터를 조회

나이가 22세 이상인 학생만 조회

name 이 “홍길동”인 학생만 조회

📌 문제 4 — UPDATE 연습
✔ 요구사항
id = 2 인 학생의 나이를 25로 수정하시오.

📌 문제 5 — DELETE 연습
✔ 요구사항
id = 3 번 학생 데이터를 삭제하는 DELETE 문을 작성하시오.
📌 문제 6 — PRIMARY KEY 이해 문제
다음과 같은 테이블을 가정하시오:
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

아래 데이터 INSERT 시 발생할 문제를 설명하시오.
INSERT INTO books (book_id, title, price)
VALUES (1, '책 A', 10000);

INSERT INTO books (book_id, title, price)
VALUES (1, '책 B', 15000);

📌 질문:
어떤 에러가 발생하는가?

왜 발생하는가?

PRIMARY KEY 의 규칙을 쓰시오.

- 가이드
 + 프롬프트로 풀고, 검증
```

```
{
  "project_name": "Database_Fundamentals_Study",
  "github_repo": "study_databases",
  "prompt_id": "SQL-001",
  "title": "SQL 기초: CRUD 및 PRIMARY KEY 이해",
  "level": "Beginner",
  "problem_statement": "주어진 요구사항에 맞춰 테이블 생성, 데이터 삽입, 조회, 수정, 삭제(CRUD) 쿼리를 작성하고 PRIMARY KEY 규칙에 대한 질문에 답하시오. 모든 쿼리 결과는 실행 후 검증되어야 합니다.",
  "tasks": [
    {
      "id": 1,
      "type": "SQL_CREATE_TABLE",
      "instruction": "요구사항에 맞는 `students` 테이블의 `CREATE TABLE` 문을 작성하시오. ID는 PRIMARY KEY입니다.",
      "requirements": [
        "테이블명: students",
        "컬럼: id (INT, PRIMARY KEY)",
        "컬럼: name (VARCHAR(50))",
        "컬럼: age (INT)"
      ]
    },
    {
      "id": 2,
      "type": "SQL_INSERT",
      "instruction": "Task 1에서 생성한 `students` 테이블에 다음 세 개의 데이터를 `INSERT` 하시오.",
      "data": [
        {"id": 1, "name": "홍길동", "age": 23},
        {"id": 2, "name": "이영희", "age": 21},
        {"id": 3, "name": "박철수", "age": 26}
      ]
    },
    {
      "id": 3,
      "type": "SQL_SELECT",
      "instruction": "다음 조건들을 만족하는 세 가지 `SELECT` 쿼리를 각각 작성하시오.",
      "sub_tasks": [
        "a. `students` 테이블의 전체 데이터 조회",
        "b. 나이가 22세 이상인 학생만 조회",
        "c. name 이 '홍길동'인 학생만 조회"
      ]
    },
    {
      "id": 4,
      "type": "SQL_UPDATE",
      "instruction": "ID가 2인 학생의 `age`를 25로 수정하는 `UPDATE` 쿼리를 작성하시오."
    },
    {
      "id": 5,
      "type": "SQL_DELETE",
      "instruction": "ID가 3번인 학생 데이터를 삭제하는 `DELETE` 쿼리를 작성하시오."
    },
    {
      "id": 6,
      "type": "SQL_CONCEPT_PRIMARY_KEY",
      "instruction": "주어진 `books` 테이블에 두 번째 `INSERT` 시 발생하는 문제에 대해 설명하고 PRIMARY KEY 규칙을 정리하시오.",
      "schema": "CREATE TABLE books ( book_id INT PRIMARY KEY, title VARCHAR(100), price INT );",
      "queries": [
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);",
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);"
      ],
      "questions": [
        "어떤 에러가 발생하는가?",
        "왜 발생하는가?",
        "PRIMARY KEY의 규칙을 쓰시오."
      ]
    }
  ],
  "guide": "각 문제에 대한 SQL 쿼리를 작성하고, 예상되는 실행 결과를 명시하여 검증 과정을 포함하시오."
}
```

```
요청하신 SQL 관련 문제를 포함하는 VS Code Gemini용 **JSON 프롬프트**와 해당 내용을 정리한 **Markdown 파일**을 생성합니다. 본인의 의견은 제외하고 파일 내용만 출력합니다.

-----

## 1\. SQL 쿼리 구현 및 검증 프롬프트 (JSON 파일)

이 JSON 파일은 Gemini에게 SQL 문제를 풀고 결과를 검증하도록 지시합니다.

```json
{
  "project_name": "Database_Fundamentals_Study",
  "github_repo": "study_databases",
  "prompt_id": "SQL-001",
  "title": "SQL 기초: CRUD 및 PRIMARY KEY 이해",
  "level": "Beginner",
  "problem_statement": "주어진 요구사항에 맞춰 테이블 생성, 데이터 삽입, 조회, 수정, 삭제(CRUD) 쿼리를 작성하고 PRIMARY KEY 규칙에 대한 질문에 답하시오. 모든 쿼리 결과는 실행 후 검증되어야 합니다.",
  "tasks": [
    {
      "id": 1,
      "type": "SQL_CREATE_TABLE",
      "instruction": "요구사항에 맞는 `students` 테이블의 `CREATE TABLE` 문을 작성하시오. ID는 PRIMARY KEY입니다.",
      "requirements": [
        "테이블명: students",
        "컬럼: id (INT, PRIMARY KEY)",
        "컬럼: name (VARCHAR(50))",
        "컬럼: age (INT)"
      ]
    },
    {
      "id": 2,
      "type": "SQL_INSERT",
      "instruction": "Task 1에서 생성한 `students` 테이블에 다음 세 개의 데이터를 `INSERT` 하시오.",
      "data": [
        {"id": 1, "name": "홍길동", "age": 23},
        {"id": 2, "name": "이영희", "age": 21},
        {"id": 3, "name": "박철수", "age": 26}
      ]
    },
    {
      "id": 3,
      "type": "SQL_SELECT",
      "instruction": "다음 조건들을 만족하는 세 가지 `SELECT` 쿼리를 각각 작성하시오.",
      "sub_tasks": [
        "a. `students` 테이블의 전체 데이터 조회",
        "b. 나이가 22세 이상인 학생만 조회",
        "c. name 이 '홍길동'인 학생만 조회"
      ]
    },
    {
      "id": 4,
      "type": "SQL_UPDATE",
      "instruction": "ID가 2인 학생의 `age`를 25로 수정하는 `UPDATE` 쿼리를 작성하시오."
    },
    {
      "id": 5,
      "type": "SQL_DELETE",
      "instruction": "ID가 3번인 학생 데이터를 삭제하는 `DELETE` 쿼리를 작성하시오."
    },
    {
      "id": 6,
      "type": "SQL_CONCEPT_PRIMARY_KEY",
      "instruction": "주어진 `books` 테이블에 두 번째 `INSERT` 시 발생하는 문제에 대해 설명하고 PRIMARY KEY 규칙을 정리하시오.",
      "schema": "CREATE TABLE books ( book_id INT PRIMARY KEY, title VARCHAR(100), price INT );",
      "queries": [
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);",
        "INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);"
      ],
      "questions": [
        "어떤 에러가 발생하는가?",
        "왜 발생하는가?",
        "PRIMARY KEY의 규칙을 쓰시오."
      ]
    }
  ],
  "guide": "각 문제에 대한 SQL 쿼리를 작성하고, 예상되는 실행 결과를 명시하여 검증 과정을 포함하시오."
}
```


```
## 2\. SQL 쿼리 구현 및 검증 프롬프트 (Markdown 파일)

이 Markdown 파일은 JSON 프롬프트의 내용을 보기 쉽게 정리한 문서입니다.

markdown
# 📚 SQL 기초: CRUD 및 PRIMARY KEY 이해

*GitHub Repo: `study_databases`* | *Prompt ID: `SQL-001`* | *Level: Beginner*

## 📝 문제 개요

주어진 요구사항에 맞춰 **테이블 생성, 데이터 삽입, 조회, 수정, 삭제(CRUD)** 쿼리를 작성하고 **PRIMARY KEY** 규칙에 대한 질문에 답하시오.



## 📌 문제 1 — 테이블 생성 (PRIMARY KEY 기초)

요구사항에 맞는 `CREATE TABLE` 문을 작성하시오.

| 항목 | 상세 |
| :--- | :--- |
| **테이블명** | `students` |
| **컬럼 1** | `id` (INT, **PRIMARY KEY**) |
| **컬럼 2** | `name` (VARCHAR(50)) |
| **컬럼 3** | `age` (INT) |

### 쿼리:

sql
 CREATE TABLE students ...




## 📌 문제 2 — CREATE (INSERT) 기초

위 `students` 테이블에 다음 데이터를 `INSERT` 하시오.

| id | name | age |
| :---: | :---: | :---: |
| 1 | 홍길동 | 23 |
| 2 | 이영희 | 21 |
| 3 | 박철수 | 26 |

### 쿼리:

sql
INSERT INTO students ...




## 📌 문제 3 — READ (SELECT) 기본 조회

다음 조건들을 만족하는 세 가지 `SELECT` 쿼리를 각각 작성하시오.

### a. 전체 데이터 조회

`students` 테이블의 전체 데이터를 조회합니다.

sql
SELECT 쿼리 (전체)


### b. 조건 조회 (WHERE Age)

나이가 22세 이상인 학생만 조회합니다.

sql
SELECT 쿼리 (나이 >= 22)


### c. 조건 조회 (WHERE Name)

`name`이 "홍길동"인 학생만 조회합니다.

sql
SELECT 쿼리 (이름 = '홍길동')




## 📌 문제 4 — UPDATE 연습

ID가 2인 학생의 나이를 25로 수정하는 `UPDATE` 쿼리를 작성하시오.

### 쿼리:

sql
UPDATE students SET ... WHERE id = 2




## 📌 문제 5 — DELETE 연습

ID가 3번인 학생 데이터를 삭제하는 `DELETE` 쿼리를 작성하시오.

### 쿼리:

sql
DELETE FROM students ... WHERE id = 3




## 📌 문제 6 — PRIMARY KEY 이해 문제

다음과 같은 테이블과 쿼리를 가정하시오.

sql
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);

INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);
-- 여기서 문제가 발생
INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);


### 질문 및 답변:

1.  **어떤 에러가 발생하는가?**
2.  **왜 발생하는가?**
3.  **PRIMARY KEY의 규칙을 쓰시오.**

<!-- end list -->

```

```
# SQL 기초: CRUD 및 PRIMARY KEY 이해

- **Project:** Database_Fundamentals_Study
- **GitHub Repo:** study_databases
- **Prompt ID:** SQL-001
- **Level:** Beginner

## 문제 설명

주어진 요구사항에 맞춰 테이블 생성, 데이터 삽입, 조회, 수정, 삭제(CRUD) 쿼리를 작성하고 PRIMARY KEY 규칙에 대한 질문에 답하시오. 모든 쿼리 결과는 실행 후 검증되어야 합니다.

## 가이드

각 문제에 대한 SQL 쿼리를 작성하고, 예상되는 실행 결과를 명시하여 검증 과정을 포함하시오.
```

