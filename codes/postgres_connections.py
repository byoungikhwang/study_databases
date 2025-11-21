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
with conn.cursor() as cursor :
    # cursor.execute("INSERT INTO users_uuid_name (name) VALUES ('from code');")
    # cursor.execute("""UPDATE users_uuid_name
    #                 SET name = 'code Name'
    #                 WHERE id_name = '9a328b2c-f195-499e-a3d0-c76ca59be4dd';""")
    # cursor.execute("""DELETE FROM users_uuid_name
    #                 WHERE id_name = '84afbbf1-c3f4-4508-bf2d-c84455eb4a49';""")
    cursor.execute("SELECT name, id_name FROM users_uuid_name;")
    records = cursor.fetchall()
    for record in records :
        print(record)
        print(f'{record[0]} : {record[1]}')
conn.commit()


# import psycopg2
# import os

# """PostgreSQL 데이터베이스에 연결합니다."""
# db_host = "db_postgresql"
# db_port = "5432"
# db_name = "main_db"
# db_user = "admin"
# db_password = "admin123"

# conn = None # conn을 초기화하여 finally 블록에서 사용 가능하도록 함

# try:
#     conn = psycopg2.connect(
#         host=db_host,
#         port=db_port,
#         dbname=db_name,
#         user=db_user,
#         password=db_password
#     )
#     print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

#     # --- 1. UPDATE 작업 ---
#     with conn.cursor() as cursor:
#         cursor.execute("""UPDATE users_uuid_name
#                         SET name = 'code Name'
#                         WHERE id_name = 'f3e223ca-69d2-4432-bcaa-d7b01b44dbf9';""")

#     # --- 2. DELETE 작업 ---
#     with conn.cursor() as cursor:
#         cursor.execute("""
#             DELETE FROM students
#             WHERE id_name = '3';
#         """)
        
#     # 변경 사항 커밋 (UPDATE, DELETE 후)
#     conn.commit()
#     print("UPDATE 및 DELETE 작업 커밋 완료.")

#     # --- 3. SELECT 작업 (오류 수정) ---
#     # NameError 및 오타 방지를 위해 새로운 with 블록을 사용합니다.
#     with conn.cursor() as cursor:
#         # 오타 수정: exectue -> execute, users_uuid_namd -> users_uuid_name
#         cursor.execute("SELECT name, id_name FROM users_uuid_name;") 
        
#         records = cursor.fetchall()
        
#         # 4. 반복문 들여쓰기 수정
#         print("\n--- 조회 결과 ---")
#         for record in records:
#             print(record)
#             print(f'{record[0]}: {record[1]}')
            
# except psycopg2.Error as e:
#     print(f"데이터베이스 오류 발생: {e}")
#     if conn:
#         conn.rollback() # 오류 발생 시 롤백
        
# finally:
#     if conn:
#         conn.close()
#         print("\n데이터베이스 연결 종료.")