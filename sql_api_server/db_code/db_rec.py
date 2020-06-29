#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jia-Yu Lu <jeanie0807@gmail.com>'


import sqlite3


def main():
    conn = sqlite3.connect('../data/db.sqlite',
                           detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()
    user_id = 1

    rec_director_result = rec_director(c, user_id)
    # print(rec_director_result)

    rec_actor_result = rec_actor(c, user_id)
    # print(rec_actor_result)

    rec_by_model_result = rec_by_model(c, user_id)
    # print(rec_by_model_result)

    conn.commit()
    conn.close()


# Find recommended movies with the same director based on user click table and sort by user's click
def rec_director(c, user_id):
    rec_director_list = []
    rec_director_res = c.execute('''
                SELECT DISTINCT movie.*
                FROM click, director AS adirector, director AS bdirector, movie
                WHERE click.user_id=?
                AND click.movie_id=adirector.movie_id
                AND adirector.director=bdirector.director
                AND movie.movie_id=bdirector.movie_id
                GROUP BY bdirector.movie_id
                ORDER BY MAX(click.click) DESC
            ''', (user_id, ))
    for row in rec_director_res:
        rec_director_list.append(row)
    return rec_director_list


# Find recommended movies with the same actor_actress based on user click table and sort by user's click
def rec_actor(c, user_id):
    rec_actor_list = []
    rec_actor_res = c.execute('''
                SELECT DISTINCT movie.*
                FROM click, actor AS aactor, actor AS bactor, movie
                WHERE click.user_id=?
                AND click.movie_id=aactor.movie_id
                AND aactor.actor_actress=bactor.actor_actress
                AND movie.movie_id=bactor.movie_id
                GROUP BY bactor.movie_id
                ORDER BY MAX(click.click) DESC
            ''', (user_id, ))
    for row in rec_actor_res:
        rec_actor_list.append(row)
    return rec_actor_list


# Find recommended movies with model predicted
def rec_by_model(c, user_id):
    rec_by_model_list = []
    rec_by_model_res = c.execute('''
                SELECT DISTINCT movie.*
                FROM model, movie
                WHERE model.user_id=?
                AND model.movie_id=movie.movie_id
            ''', (user_id, ))
    for row in rec_by_model_res:
        rec_by_model_list.append(row)
    return rec_by_model_list


if __name__ == '__main__':
    main()
