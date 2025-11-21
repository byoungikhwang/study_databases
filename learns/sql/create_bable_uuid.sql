# 1. UUID 확장 기능 활성화 및 테이블 생성
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE TABLE users_uuid_name (
  id_name UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  name VARCHAR(100)
);

INSERT INTO users_uuid_name (name) VALUES ('Alice');

SELECT * FROM users_uuid_name;

INSERT INTO users_uuid_name (name)
VALUES ('alice'), ('bob'), ('charlie');

UPDATE users_uuid_name
    SET name = 'saintjin Name'
    WHERE id_name = '9d888b8b-a623-4deb-a8ca-5cad52cc5341';
