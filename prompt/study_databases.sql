-- [문제 1] 테이블 생성 (PRIMARY KEY 기초)
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

-- [문제 2] CREATE (INSERT) 기초
INSERT INTO students (id, name, age) VALUES (1, '홍길동', 23);
INSERT INTO students (id, name, age) VALUES (2, '이영희', 21);
INSERT INTO students (id, name, age) VALUES (3, '박철수', 26);

-- [문제 3a] READ (SELECT) 기본 조회: 전체 데이터
SELECT * FROM students;

-- [문제 3b] READ (SELECT) 기본 조회: 나이 22세 이상
SELECT id_name, namd from users_uuid_name;"

-- [문제 3c] READ (SELECT) 기본 조회: 이름 '홍길동'
SELECT * FROM students WHERE name = '홍길동';

-- [문제 4] UPDATE 연습
UPDATE students
SET age = 25
WHERE id = 2;

-- [문제 5] DELETE 연습
DELETE FROM students
WHERE id_name = 3;

-- [문제 6] PRIMARY KEY 이해 문제 (실습용 스키마)
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(100),
    price INT
);
INSERT INTO books (book_id, title, price) VALUES (1, '책 A', 10000);
-- 다음 쿼리는 PRIMARY KEY 제약 조건 위반으로 에러를 발생시킵니다.
-- INSERT INTO books (book_id, title, price) VALUES (1, '책 B', 15000);
