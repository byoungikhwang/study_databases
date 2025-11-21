import psycopg2
import psycopg2.extras
import os

# --- Database Connection ---
# 환경 변수 또는 직접 값을 사용하여 연결 정보를 설정합니다.
# 예: os.environ.get('DB_NAME', 'your_db')
DB_NAME = os.environ.get('DB_NAME', 'mydatabase')
DB_USER = os.environ.get('DB_USER', 'myuser')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'mypassword')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '5432')

def get_connection():
    """PostgreSQL 데이터베이스에 연결합니다."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the database. Please check your connection settings.")
        print(f"Details: {e}")
        return None

def execute_query(conn, query, params=None, fetch=None):
    """주어진 쿼리를 실행하고 결과를 반환합니다."""
    with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
        cursor.execute(query, params)
        conn.commit()
        if fetch == 'one':
            return cursor.fetchone()
        if fetch == 'all':
            return cursor.fetchall()

def main():
    """메인 실행 함수"""
    conn = get_connection()
    if not conn:
        return

    try:
        # --- 초기화: 이전 테이블 삭제 (실습을 위해) ---
        print("--- 1. Initializing: Dropping existing 'students' and 'books' tables if they exist ---")
        execute_query(conn, "DROP TABLE IF EXISTS students;")
        execute_query(conn, "DROP TABLE IF EXISTS books;")
        print("Tables dropped successfully.\n")

        # --- 문제 1: CREATE TABLE ---
        # UUID 함수를 사용하기 위해 uuid-ossp 확장 활성화
        print("--- 2. Task 1: Creating 'students' table with UUID primary key ---")
        execute_query(conn, "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";")
        create_table_query = """
        CREATE TABLE students (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            name VARCHAR(50) NOT NULL,
            age INT NOT NULL
        );
        """
        execute_query(conn, create_table_query)
        print("Table 'students' created successfully.\n")

        # --- 문제 2: INSERT ---
        print("--- 3. Task 2: Inserting initial data into 'students' table ---")
        insert_query = "INSERT INTO students (name, age) VALUES (%s, %s);"
        students_to_insert = [
            ("홍길동", 23),
            ("이영희", 21),
            ("박철수", 26)
        ]
        for student in students_to_insert:
            execute_query(conn, insert_query, student)
        print(f"{len(students_to_insert)} students inserted successfully.\n")

        # --- 문제 3: SELECT ---
        print("--- 4. Task 3: Selecting data ---")
        # a. 전체 데이터 조회
        print("a. All students:")
        all_students = execute_query(conn, "SELECT id, name, age FROM students;", fetch='all')
        for student in all_students:
            print(dict(student))

        # b. 나이가 22세 이상인 학생만 조회
        print("\nb. Students older than or equal to 22:")
        older_students = execute_query(conn, "SELECT id, name, age FROM students WHERE age >= 22;", fetch='all')
        for student in older_students:
            print(dict(student))

        # c. name 이 '홍길동'인 학생만 조회
        print("\nc. Student named '홍길동':")
        gildong = execute_query(conn, "SELECT id, name, age FROM students WHERE name = %s;", ('홍길동',), fetch='one')
        print(dict(gildong) if gildong else "Not Found")
        print("\n")


        # --- 문제 4: UPDATE ---
        print("--- 5. Task 4: Updating a student's age ---")
        # '이영희'의 UUID 확보
        younghee = execute_query(conn, "SELECT id FROM students WHERE name = %s;", ('이영희',), fetch='one')
        if younghee:
            younghee_id = younghee['id']
            print(f"Found '이영희' with UUID: {younghee_id}")
            # age를 25로 수정
            update_query = "UPDATE students SET age = %s WHERE id = %s;"
            execute_query(conn, update_query, (25, younghee_id))
            print("'이영희''s age updated to 25.")

            # 변경 확인
            updated_younghee = execute_query(conn, "SELECT * FROM students WHERE id = %s;", (younghee_id,), fetch='one')
            print("Verified update:", dict(updated_younghee))
        else:
            print("'이영희' not found.")
        print("\n")


        # --- 문제 5: DELETE ---
        print("--- 6. Task 5: Deleting a student ---")
        # '박철수'의 UUID 확보
        cheolsu = execute_query(conn, "SELECT id FROM students WHERE name = %s;", ('박철수',), fetch='one')
        if cheolsu:
            cheolsu_id = cheolsu['id']
            print(f"Found '박철수' with UUID: {cheolsu_id}")
            # 데이터 삭제
            delete_query = "DELETE FROM students WHERE id = %s;"
            execute_query(conn, delete_query, (cheolsu_id,))
            print("'박철수' deleted from the table.")

            # 삭제 확인
            deleted_cheolsu = execute_query(conn, "SELECT * FROM students WHERE id = %s;", (cheolsu_id,), fetch='one')
            print("Verification (should be None):", deleted_cheolsu)
        else:
            print("'박철수' not found.")
        print("\n")

        # --- 최종 데이터 확인 ---
        print("--- 7. Final data in 'students' table ---")
        final_data = execute_query(conn, "SELECT * FROM students;", fetch='all')
        for row in final_data:
            print(dict(row))
        print("\n")

    finally:
        # --- 연결 종료 ---
        if conn:
            conn.close()
            print("Database connection closed.")


# --- 문제 6: SQL_CONCEPT_PRIMARY_KEY ---
"""
- 에러 유형: UNIQUE constraint violation 또는 PRIMARY KEY constraint violation (PostgreSQL에서는 'unique_violation')
- 원인:
  PRIMARY KEY 제약 조건은 테이블의 각 행을 고유하게 식별하는 역할을 합니다. 따라서 PRIMARY KEY로 지정된 컬럼(`book_id`)은 테이블 내에서 **중복된 값을 가질 수 없습니다.**
  첫 번째 INSERT 쿼리에서 `book_id`에 값 `1`을 이미 사용했기 때문에, 두 번째 INSERT 쿼리에서 동일한 `book_id` 값 `1`을 다시 삽입하려고 시도하면 중복 키(duplicate key) 오류가 발생합니다.
- PRIMARY KEY 규칙:
  1. **고유성 (Uniqueness)**: PRIMARY KEY 컬럼의 모든 값은 고유해야 하며, 중복될 수 없다.
  2. **NOT NULL**: PRIMARY KEY 컬럼은 NULL 값을 허용하지 않는다. 모든 행은 반드시 PRIMARY KEY 값을 가져야 한다.
  이 두 가지 규칙을 통해 데이터의 무결성을 보장하고 각 행을 안정적으로 참조할 수 있게 됩니다.
"""

if __name__ == '__main__':
    main()
