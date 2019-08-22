import sqlite3


def hello():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    # cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    cursor.execute('insert into user (id, name) values (\'\', \'Michael\')')
    print(cursor.rowcount)
    cursor.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    hello()
