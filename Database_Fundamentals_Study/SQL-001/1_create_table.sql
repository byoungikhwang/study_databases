-- Task 1: 요구사항에 맞는 `students` 테이블의 `CREATE TABLE` 문을 작성하시오. ID는 PRIMARY KEY입니다.
-- 테이블명: students
-- 컬럼: id (INT, PRIMARY KEY)
-- 컬럼: name (VARCHAR(50))
-- 컬럼: age (INT)

CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
