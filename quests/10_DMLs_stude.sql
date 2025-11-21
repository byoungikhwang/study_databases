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
-- 2. 초기 데이터 삽입 (INSERT)
-- 요구사항: 위 데이터를 테이블에 추가하라
INSERT INTO news_articles (title, url, author, published_at) VALUES
('AI 시대 도래', 'https://news.com/ai', '홍길동', '2025-01-01'),
('경제 성장률 상승', 'https://news.com/economy', '이영희', '2025-01-05');
-- 3. 데이터 조회 (SELECT)
-- 요구사항: author가 "홍길동"인 데이터만 조회하는 쿼리 작성
SELECT 
    id, title, url, author, published_at
FROM 
    news_articles
WHERE 
    author = '홍길동';
-- 4. 데이터 수정 (UPDATE)
-- 요구사항: 첫 번째 뉴스 제목("AI 시대 도래")을 'AI와 미래 사회의 변화'로 변경하는 UPDATE문 작성
UPDATE 
    news_articles
SET 
    title = 'AI와 미래 사회의 변화'
WHERE 
    title = 'AI 시대 도래';
-- 5. 데이터 삭제 (DELETE)
-- 요구사항: 두 번째 뉴스("경제 성장률 상승")를 삭제하는 DELETE문 작성
DELETE FROM 
    news_articles
WHERE 
    title = '경제 성장률 상승';