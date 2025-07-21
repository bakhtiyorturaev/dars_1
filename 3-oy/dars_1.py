import psycopg2
from prettytable import from_db_cursor

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="postgres",
    password="2001"
)
cursor = conn.cursor()



cursor.execute("""
                  SELECT
                        s.student_id,
                        s.name,
                        count( DISTINCT c.student_id) AS student_id_course,
                        c.course
                  FROM students s
                  FULL JOIN courses c
                  ON s.student_id = c.student_id

                  """)

cursor.execute("""
                  SELECT
                        count( DISTINCT c.student_id) AS student_id_course
                  FROM students s
                  FULL JOIN courses c
                  ON s.student_id = c.student_id

                  """)

cursor.execute('select * from courses order by student_id')


# cursor.execute('select count(DISTINCT course) from courses')
# cursor.execute('select * from courses order by course')

# cursor.execute("insert into courses values(100, 'python')")


table = from_db_cursor(cursor)
# table = cursor.fetchmany()
# for i in table:
#     print(i)
print(table)


cursor.close()
conn.close()