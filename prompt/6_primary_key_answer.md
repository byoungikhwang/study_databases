# 📌 문제 6 답변: PRIMARY KEY 이해

## 1. 어떤 에러가 발생하는가?
**`Duplicate Key Error`** 또는 **`Primary Key Constraint Violation`** 에러가 발생합니다.

## 2. 왜 발생하는가?
테이블 `books`의 `book_id` 컬럼은 **PRIMARY KEY**로 지정되어 있습니다. PRIMARY KEY는 **고유성(Uniqueness)**을 강제하기 때문에, 첫 번째 쿼리에서 이미 삽입된 `book_id` **1**을 두 번째 쿼리에서 다시 삽입하려고 시도하면 데이터베이스 시스템이 이를 거부하며 에러를 발생시킵니다.

## 3. PRIMARY KEY의 규칙을 쓰시오.
1.  **고유성 (Uniqueness):** PRIMARY KEY 컬럼의 값은 테이블 내에서 **중복될 수 없습니다.**
2.  **NOT NULL:** PRIMARY KEY 컬럼의 값은 **반드시 존재**해야 하며 NULL 값을 가질 수 없습니다.
