#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jia-Yu Lu <jeanie0807@gmail.com>'


import sqlite3

conn = sqlite3.connect('../data/db.sqlite',
                       detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()

c.execute('''
    CREATE TABLE "user" (
        "user_id"            INTEGER                            NOT NULL,
        "name"         TEXT            NOT NULL,
        "account"      TEXT       NOT NULL,
        "password"         TEXT            NOT NULL,
        "gender"         TEXT            DEFAULT NULL,
        "md5"         TEXT            NOT NULL,
        PRIMARY KEY("user_id")
    );
''')


c.execute('''
    CREATE TABLE "click" (
        "user_id"            INTEGER                            NOT NULL,
        "movie_id"    INTEGER                            NOT NULL,
        "rating"         INTEGER            DEFAULT NULL,
        "click"    INTEGER       DEFAULT NULL,
        PRIMARY KEY("user_id", "movie_id"),
        FOREIGN KEY("user_id") REFERENCES user("user_id"),
        FOREIGN KEY("movie_id") REFERENCES movie("movie_id")
    );
''')


c.execute('''
    CREATE TABLE "movie" (
        "movie_id"      INTEGER                             NOT NULL,
        "year"          INTEGER                        DEFAULT NULL,
        "title"     TEXT                          NOT NULL,
        "rating"     INTEGER                          DEFAULT NULL,
        "storyline"  TEXT                          DEFAULT NULL,
        "summary_text" TEXT                          DEFAULT NULL,
        "imgurl"  TEXT                          DEFAULT NULL,
        PRIMARY KEY("movie_id")
    );
''')


c.execute('''
    CREATE TABLE "actor" (
        "movie_id"      INTEGER                             NOT NULL,
        "actor_actress"          TEXT                        NOT NULL,
        PRIMARY KEY("movie_id", "actor/actress"),
        FOREIGN KEY("movie_id") REFERENCES movie("movie_id")
    );
''')

c.execute('''
    CREATE TABLE "company" (
        "movie_id"      INTEGER                             NOT NULL,
        "production_company"          TEXT                        NOT NULL,
        PRIMARY KEY("movie_id", "production_company"),
        FOREIGN KEY("movie_id") REFERENCES movie("movie_id")
    );
''')

c.execute('''
    CREATE TABLE "director" (
        "movie_id"      INTEGER                             NOT NULL,
        "director"          TEXT                        NOT NULL,
        PRIMARY KEY("movie_id", "director"),
        FOREIGN KEY("movie_id") REFERENCES movie("movie_id")
    );
''')

# c.execute('''
#     CREATE TABLE "screenwriter" (
#         "movie_id"      INTEGER                             NOT NULL,
#         "screenwriter"          TEXT                        NOT NULL,
#         PRIMARY KEY("movie_id", "screenwriter"),
#         FOREIGN KEY("movie_id") REFERENCES movie("movie_id")
#     );
# ''')

c.execute('''
    CREATE TABLE "type" (
        "movie_id"      INTEGER                             NOT NULL,
        "type"          TEXT                        NOT NULL,
        PRIMARY KEY("movie_id", "type"),
        FOREIGN KEY("movie_id") REFERENCES movie("movie_id")
    );
''')


conn.commit()
conn.close()
