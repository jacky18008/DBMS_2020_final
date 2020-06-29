#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jia-Yu Lu <jeanie0807@gmail.com>'


import sqlite3


def main():
    conn = sqlite3.connect('../data/db.sqlite',
                           detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()

    mword = 'The Duck'
    mtype = 'Animation Children'
    mcomany = 'Zucker Brothers Productions'

    search_title_result = search_title(c, mword)
    # print(search_title_result)

    search_type_result = search_type(c, mtype)
    # print(search_type_result)

    search_company_result = search_company(c, mcomany)
    # print(search_company_result)

    conn.commit()
    conn.close()


def search_title(c, mword):
    search_title_result = set()
    word_list = mword.split(' ')
    for word in word_list:
        for row in c.execute(f'SELECT * FROM movie WHERE movie.title like "%{word}%" OR movie.storyline like "%{word}%"'):
            search_title_result.add(row)

    return search_title_result


def search_type(c, mtype):
    search_type_result = set()
    type_list = mtype.split(' ')
    for atype in type_list:
        search_type_q = c.execute(f'''
                SELECT DISTINCT movie.*
                FROM movie, type
                WHERE type.type like "%{atype}%" AND type.movie_id=movie.movie_id
            ''')
        for row in search_type_q:
            search_type_result.add(row)

    return search_type_result


def search_company(c, mcompany):
    search_company_result = set()
    company_list = mcompany.split(' ')
    for acompany in company_list:
        search_company_q = c.execute(f'''
                SELECT DISTINCT movie.*
                FROM movie, company
                WHERE company.production_company like "%{acompany}%" AND company.movie_id=movie.movie_id
            ''')
        for row in search_company_q:
            search_company_result.add(row)

    return search_company_result


if __name__ == '__main__':
    main()
