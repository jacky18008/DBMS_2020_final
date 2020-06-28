#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jia-Yu Lu <jeanie0807@gmail.com>'


import sqlite3
import hashlib

md5 = hashlib.md5()


def main():
    conn = sqlite3.connect('../data/db.sqlite',
                           detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()

    # user_account = 'Rene463'
    # user_account_info = check_user_account(c, user_account)
    # print(user_account_info)

    # name = 'Mary'
    account = 'aaaa'
    # password = 'asdf'
    # gender = 'F'
    # create_new_user(c, name, account, password, gender)

    # update_dic = {'name': 'aaa', 'password': 'ssss'}
    # update_user_info(c, account, update_dic)

    delete_user(c, account)

    conn.commit()
    conn.close()


# find user info data
def check_user_account(c, user_account):
    for row in c.execute('SELECT * FROM user WHERE account = ?', (user_account,)):
        user_id = row[0]
        name = row[1]
        account = row[2]
        password = row[3]
        gender = row[4]
        md5 = row[5]
    # print(row)
    return row


# create new user
def create_new_user(c, name, account, password, gender):
    user_count = c.execute("SELECT COUNT() FROM user").fetchone()[0] + 1
    decode_data = account + password
    md5.update(decode_data.encode("utf-8"))
    h = md5.hexdigest()
    c.execute(
        'INSERT OR IGNORE INTO user (user_id, name, account, password, gender, md5) VALUES (?, ?, ?, ?, ?, ?)',
        (user_count, name, account, password, gender, h)
    )
    # check_user_account(c, account)


# update user data
def update_user_info(c, account, update_dic):
    info_dic = {}
    user_account_info = check_user_account(c, account)
    c.execute('select * from user')
    colnames = c.description
    for index, row in enumerate(colnames):
        info_dic[row[0]] = user_account_info[index]
    for mod_data in update_dic:
        info_dic[mod_data] = update_dic[mod_data]

    decode_data = info_dic['account'] + info_dic['password']
    md5.update(decode_data.encode("utf-8"))
    h = md5.hexdigest()

    c.execute(
        '''
                UPDATE user
                SET name=?,
                account=?,
                password=?,
                gender=?,
                md5=?
                WHERE user_id=?
            ''',
        (info_dic['name'], info_dic['account'], info_dic['password'],
         info_dic['gender'], h, info_dic['user_id'],),
    )
    # check_user_account(c, account)


# delete user
def delete_user(c, account):
    # user_count = c.execute("SELECT COUNT() FROM user").fetchone()[0]
    # print(user_count)
    user_account_info = check_user_account(c, account)
    c.execute('DELETE FROM user WHERE user_id=?', (user_account_info[0], ))
    # user_count = c.execute("SELECT COUNT() FROM user").fetchone()[0]
    # print(user_count)


if __name__ == '__main__':
    main()
