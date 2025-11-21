import psycopg2
import os

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
with conn.cursor() as cursor :
    cursor.execute("""UPDATE users_uuid_name
                    SET name = 'code Name'
                    WHERE id_name = 'f3e223ca-69d2-4432-bcaa-d7b01b44dbf9';""")
conn.commit()

    # cursor.execute("""UPDATE users_uuid_name
    #                 SET name = 'code Name'
    #                 WHERE id_name = '9a328b2c-f195-499e-a3d0-c76ca59be4dd';""")