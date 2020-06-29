#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Jia-Yu Lu <jeanie0807@gmail.com>'

import csv
import json

f = open('model.txt', 'w')
print('user_id, movie_id', file=f)

with open('../data/model.json') as fin:
    data = json.load(fin)
    for id_item in data:
        id_item_s = id_item.split('user')[1]
        for item in data[id_item]:
            item_s = item.split('item')[1]
            print(f'{id_item_s[1:]}, {item_s[1:]}', file=f)

f.close()
