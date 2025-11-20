-- 4. 데이터 수정 (UPDATE)
-- 요구사항: 첫 번째 뉴스 제목("AI 시대 도래")을 'AI와 미래 사회의 변화'로 변경하는 UPDATE문 작성
UPDATE 
    news_articles
SET 
    title = 'AI와 미래 사회의 변화'
WHERE 
    title = 'AI 시대 도래';
