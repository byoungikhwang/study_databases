-- 3. 데이터 조회 (SELECT)
-- 요구사항: author가 "홍길동"인 데이터만 조회하는 쿼리 작성
SELECT 
    id, title, url, author, published_at
FROM 
    news_articles
WHERE 
    author = '홍길동';
