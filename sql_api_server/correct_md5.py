import sqlite3
import hashlib

def hash_function(account, password):
    plain_text = str(account) + str(password)
    hash_text =  hashlib.md5(plain_text.encode('latin1')).hexdigest()
    return hash_text


def start_sql_connection():
    conn = sqlite3.connect('db.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
    return conn



conn = start_sql_connection()

users = []
for cursor in conn.execute('select user_id, account, password from user'):
    this_user = ( hash_function(cursor[1], cursor[2]), cursor[0] )
    users.append(this_user)

conn.executemany("update user set md5=? where user_id=?", users)
conn.commit()
conn.close()
