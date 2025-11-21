```
# 🐍 Python(psycopg2)을 이용한 PostgreSQL CRUD (UUID PK 적용)

*GitHub Repo: `study_databases`* | *Prompt ID: `PYTHON-SQL-DML-001`* | *Level: Intermediate*

## 📝 문제 개요

PostgreSQL과 Python(`psycopg2`)을 사용하여 'students' 테이블에 대한 CRUD 작업을 수행하고, UUID Primary Key를 다루는 코드를 **`quests/10_DMLs_codes.py`** 파일 하나에 통합하여 작성하시오.

---

## 🛠️ 참조 코드 (Reference Code)

```python
import psycopg2

"""PostgreSQL 데이터베이스에 연결합니다."""
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)
print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")
# --------------------------------------------------------
# [여기에 문제 1~5 코드를 작성]
# --------------------------------------------------------
conn.commit()
print("모든 트랜잭션이 커밋되었습니다.")
```