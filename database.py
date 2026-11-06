
import sqlite3

def create_table():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            python INTEGER,
            java INTEGER,
            sql INTEGER,
            maths INTEGER,
            english INTEGER,
            total INTEGER,
            average REAL,
            grade TEXT,
            status TEXT
        )
    """)

    conn.commit()
    conn.close()


def add_student(data):
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, python, java, sql, maths, english,
         total, average, grade, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()


def get_students():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    students = cursor.fetchall()

    conn.close()
    return students
