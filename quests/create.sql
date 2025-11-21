-- 📌 문제 1: 뉴스 스크래핑 테이블 (news_articles) DML 연습 쿼리

-- 1. 테이블 정의 (CREATE TABLE).
-- Row 식별을 위한 id 컬럼(PRIMARY KEY)과 요청된 컬럼을 포함합니다.
-- Error Fix: AUTO_INCREMENT 대신 SERIAL PRIMARY KEY를 사용하여 PostgreSQL/SQLite 등에서 자동 증가를 지원합니다.
CREATE TABLE news_articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(500) NOT NULL,
    url VARCHAR(500) NOT NULL,
    author VARCHAR(500),
    published_at VARCHAR(500) -- 날짜 타입은 VARCHAR(500)으로 지정
);
