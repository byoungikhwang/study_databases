import psycopg2

def execute_and_print(cursor, query):
    """주어진 SQL 쿼리를 실행하고 결과를 출력합니다."""
    print("---")
    print(f"Executing query: {query}")
    try:
        cursor.execute(query)
        if cursor.description:
            records = cursor.fetchall()
            print("Query results:")
            for record in records:
                print(record)
        else:
            print(f"{cursor.rowcount} rows affected.")
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")

"""PostgreSQL 데이터베이스에 연결합니다."""
db_host = "db_postgresql"
db_port = "5432"
db_name = "main_db"
db_user = "admin"
db_password = "admin123"

conn = None
try:
    conn = psycopg2.connect(
        host=db_host,
        port=db_port,
        dbname=db_name,
        user=db_user,
        password=db_password
    )
    print("PostgreSQL 데이터베이스에 성공적으로 연결되었습니다.")

    with conn.cursor() as cursor:
        # INSERT, UPDATE, DELETE, SELECT 쿼리를 각각 실행하고 결과를 출력합니다.
        execute_and_print(cursor, "INSERT INTO users_uuid_name (name) VALUES ('from code');")
        execute_and_print(cursor, """UPDATE users_uuid_name
                        SET name = 'code Name'
                        WHERE id_name = '9a328b2c-f195-499e-a3d0-c76ca59be4dd';""")
        execute_and_print(cursor, """DELETE FROM users_uuid_name
                        WHERE id_name = '84afbbf1-c3f4-4508-bf2d-c84455eb4a49';""")
        execute_and_print(cursor, "SELECT name, id_name FROM users_uuid_name;")

    conn.commit()
    print("\n모든 변경 사항이 커밋되었습니다.")

except psycopg2.Error as e:
    print(f"데이터베이스 오류 발생: {e}")
    if conn:
        conn.rollback()
        print("오류가 발생하여 변경 사항을 롤백했습니다.")

finally:
    if conn:
        conn.close()
        print("\n데이터베이스 연결이 종료되었습니다.")