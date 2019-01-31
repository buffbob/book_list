import sqlite3


def init_connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id integer PRIMARY KEY, title text, "
                "author text, year integer, isbn integer)")

    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM booK WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(id_num):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id =?", (id_num,))
    conn.commit()
    conn.close()


def update(id_num, title, author, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id =?", (title, author, year, isbn, id_num))
    conn.commit()
    conn.close()




init_connect()

# This is for testing to console
#insert('Education of Little Tree', 'Forrest Gump', 1967, 345799967)
#insert("Meaning of Tao", "Lzo Tzu", 1000, 1)
#delete()
#print(view())

