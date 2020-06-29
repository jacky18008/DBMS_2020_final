#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jia-Yu Lu <jeanie0807@gmail.com>'


import sqlite3


def main():
    conn = sqlite3.connect('../data/db.sqlite',
                           detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()

    user_id = 1
    movie_id = 1357
    # click_info = check_click(c, user_id, movie_id)
    # click(c, user_id, movie_id)
    click_not_in(c, user_id, movie_id)
    # print(click_info)

    conn.commit()
    conn.close()


# find click data
def check_click(c, user_id, movie_id):
    check_click_result = []
    for row in c.execute('SELECT * FROM click WHERE user_id = ? AND movie_id = ?', (user_id, movie_id)):
        check_click_result.append(row)
    # print(check_click_result)
    return check_click_result[0]


# update click data
def click(c, user_id, movie_id):
    check_click_result = list(check_click(c, user_id, movie_id))
    # print(check_click_result)
    check_num = check_click_result[3] + 1
    # print(check_num)

    c.execute(
        '''
                UPDATE click
                SET click=?
                WHERE user_id=? AND movie_id = ?
            ''',
        (check_num, user_id, movie_id),
    )


# insert click data
def click_not_in(c, user_id, movie_id):
    c.execute(
        'INSERT OR IGNORE INTO click (user_id, movie_id, click) VALUES (?, ?, ?)',
        (user_id, movie_id, 1)
    )


if __name__ == '__main__':
    main()
