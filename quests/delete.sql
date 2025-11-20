-- 5. 데이터 삭제 (DELETE)
-- 요구사항: 두 번째 뉴스("경제 성장률 상승")를 삭제하는 DELETE문 작성
DELETE FROM 
    news_articles
WHERE 
    title = '경제 성장률 상승';
