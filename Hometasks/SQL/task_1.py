"""
[1] Создайте таблицу учеников (ФИО + номер группы). Заполните таблицу 10-ю записями.
Выберите записи только с четными id.
"""

import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def modify_table(conn, modify_table_sql):
    try:
        c = conn.cursor()
        c.execute(modify_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def select_table(conn, select_table_sql):
    try:
        c = conn.cursor()
        c.execute(select_table_sql)

        rows = c.fetchall()

        for row in rows:
            print(row)
    except Error as e:
        print(e)


def main():
    database = r"test_1.db"

    sql_create_projects_table = """
    CREATE TABLE Students
    (
        id INTEGER  PRIMARY KEY AUTOINCREMENT,
        fio TEXT(40),
        group_num INTEGER
    );
    """

    sql_insert = """
        INSERT INTO Students (fio, group_num) VALUES
        ('Сафонов Александр Робертович', 14),
        ('Смирнова Ева Львовна', 4),
        ('Богданов Дмитрий Даниилович', 15),
        ('Егорова Диана Никитична', 8),
        ('Маркелов Даниил Егорович', 14),
        ('Смирнов Мирон Кириллович', 8),
        ('Щербаков Макар Николаевич', 6),
        ('Мельников Юрий Александрович', 9),
        ('Орлов Михаил Дмитриевич', 10),
        ('Калинин Фёдор Иванович', 9);
        """

    sql_select = """
        SELECT * FROM Students
        WHERE id % 2 = 0;
        """

    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
        modify_table(conn, sql_insert)
        select_table(conn, sql_select)
        conn.close()
    else:
        print("Error! Cannot create the database connection.")


if __name__ == '__main__':
    main()
