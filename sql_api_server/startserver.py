import tornado.web
import tornado.ioloop
import tornado.autoreload
import requests as req
import json
import os
from api_addr import *
from util import * #hash_function, get_timestamp, start_sql_connection, search


SQL_CONNECTION = start_sql_connection()
FAST_HASH_VERIFICATION = set([r[0] for r in SQL_CONNECTION.execute('SELECT md5 FROM user')])
FAST_ACCOUNT_VERIFICATION = set([r[0] for r in SQL_CONNECTION.execute('SELECT account FROM user')])
NEW_COMER_HASH = set()


class baseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')

class hashHandler(baseHandler):
    def post(self):
        global FAST_HASH_VERIFICATION
        myhash = self.get_argument('hash', None)
        print("verifying", myhash)
        if myhash:
            if myhash in FAST_HASH_VERIFICATION:
                name = list(SQL_CONNECTION.execute('SELECT name FROM user WHERE md5=?', (myhash,)))[0][0]
                message = {'status': "valid", 'name': name}
            else:
                message = {'status': "invalid"}
        else:
            message = {'status': "invalid"}

        self.write(json.dumps(message))

class regHandler(baseHandler):
    def post(self):
        name = self.get_argument('name', None)
        account = self.get_argument('account', None)
        password = self.get_argument('password', None)
        gender = self.get_argument('gender', None)
        if name and account and password and gender:
            if account in FAST_ACCOUNT_VERIFICATION:
                message = {'status': "invalid", 'message': "account is already existed!"}
            else:
                new_hash = hash_function(account, password)
                SQL_CONNECTION.execute(
                    'INSERT OR IGNORE INTO user (name, account, password, gender, md5) VALUES (?, ?, ?, ?, ?)',
                    (name, account, password, gender, new_hash)
                ); SQL_CONNECTION.commit()
                message = {'status': "valid"}
                FAST_ACCOUNT_VERIFICATION.add(account)
                FAST_HASH_VERIFICATION.add(new_hash)
                NEW_COMER_HASH.add(new_hash)
            self.write(json.dumps(message))
        else:
            self.set_status(400)

class infoHandler(baseHandler):
    def post(self):
        myhash = self.get_argument('hash', None)
        if myhash:
            if myhash in FAST_HASH_VERIFICATION:
                result = list(SQL_CONNECTION.execute('SELECT * FROM user WHERE md5 = ?', (myhash,)))[0]
                name = result[1]
                account = result[2]
                gender = result[4]
                message = {'name': name, 'account': account, 'gender': gender}
                self.write(json.dumps(message))
            else:
                self.set_status(400)
        else:
            self.set_status(400)

class infoUpdateHandler(baseHandler):
    def post(self):
        myhash = self.get_argument('hash', None)
        if myhash:
            if myhash in FAST_HASH_VERIFICATION:
                result = list(SQL_CONNECTION.execute('SELECT * FROM user WHERE md5 = ?', (myhash,)))[0]
                pre_name = result[1]
                account = result[2]
                pre_password = result[3]
                pre_gender = result[4]

                message = {'status': 'valid'}
                new_name = self.get_argument('name', None)
                new_name = new_name if new_name else pre_name
                new_gender = self.get_argument('gender', None)
                new_gender = new_gender if new_gender else pre_gender
                new_password = self.get_argument('password', None)
                message['message'] = "Personal Info updated Successfully!"
                if new_password != "" and new_password != None:
                    new_hash = hash_function(account, new_password)
                    message['message'] = "re_login"
                    FAST_HASH_VERIFICATION.remove(myhash)
                    FAST_HASH_VERIFICATION.add(new_hash)
                else:
                    new_password = pre_password
                    new_hash = myhash
                
                SQL_CONNECTION.execute(
                    '''
                        UPDATE user
                        SET name=?,
                        password=?,
                        gender=?,
                        md5=?
                        WHERE md5=?
                    ''',
                    (new_name, new_password, new_gender, new_hash, new_hash),
                ); SQL_CONNECTION.commit() 

                self.write(json.dumps(message))
            else:
                self.set_status(400)
        else:
            self.set_status(400)

class deleteAccountHandler(baseHandler):
    def post(self):
        myhash = self.get_argument('hash', None)
        if myhash:
            if myhash in FAST_HASH_VERIFICATION:
                result = list(SQL_CONNECTION.execute('SELECT * FROM user WHERE md5 = ?', (myhash,)))[0]
                name = result[1]
                account = result[2]
                password = result[3]
                gender = result[4]
                val_name = self.get_argument('name', None) == name
                val_gender = self.get_argument('gender', None) == gender
                val_password = self.get_argument('password', None) == password
                if val_name and val_gender and val_password:
                    SQL_CONNECTION.execute('DELETE FROM user WHERE md5=?', (myhash, )); SQL_CONNECTION.commit()
                    message = {'status': 'valid', 'message': 'Your Account has been Deleted Successfully!'}
                    FAST_HASH_VERIFICATION.remove(myhash)
                    FAST_ACCOUNT_VERIFICATION.remove(account)
                else:
                    message = {'status': 'invalid', 'message': 'personal info or password may be incorrect!'}
            else:
                self.set_status(400)

            self.write(json.dumps(message))
        else:
            self.set_status(400)


class searchHandler(baseHandler):
    def post(self):
        query = self.get_argument("query", None)
        message = {'results': search(SQL_CONNECTION, query)}
        self.write(json.dumps(message))

class recHandler(baseHandler):
    def post(self):
        myhash = self.get_argument("hash", None)
        if myhash not in FAST_HASH_VERIFICATION:
            self.write(json.dumps({'results':[]}))
        else:
            if myhash in NEW_COMER_HASH:
                message = {'results': cold_recommend(SQL_CONNECTION)}
            else:
                message = {'results': recommend(SQL_CONNECTION, myhash)}
            self.write(json.dumps(message))

class clickThoughHandler(baseHandler):
    def post(self):
        try:
            mid = self.get_argument("mid", None)
            myhash = self.get_argument("hash", None)
            if myhash and mid:
                print('%s clicked %s'%(myhash, mid))
                user_id = list(SQL_CONNECTION.execute("SELECT user_id from user WHERE md5=?",(myhash,)))[0][0]
                movie_id = mid
                my_res = list(SQL_CONNECTION.execute('SELECT * FROM click WHERE user_id = ? AND movie_id = ?', (user_id, movie_id)))[0]
                is_exist = len(my_res) > 0
                if is_exist:
                    clicks = my_res[3] + 1
                    SQL_CONNECTION.execute(
                        '''
                            UPDATE click
                            SET click=?
                            WHERE user_id=? AND movie_id = ?
                        ''',
                        (clicks, user_id, movie_id),
                    )
                else:
                    SQL_CONNECTION.execute(
                        'INSERT OR IGNORE INTO click (user_id, movie_id, rating, click) VALUES (?, ?, ?, ?)',
                        (user_id, movie_id, 3, 1)
                    )
        except:
            pass
        

if __name__ == "__main__":
    application = tornado.web.Application([
            (HASH_VALIDATE_ADDR, hashHandler),
            (REGISTER_ADDR, regHandler),
            (PERSONAL_INFO_ADDR, infoHandler),
            (PERSONAL_INFO_UPDATE_ADDR, infoUpdateHandler),
            (SEARCH_MOVIE_ADDR, searchHandler),
            (RECOMMEND_MOVIE_ADDR, recHandler),
            (DELETE_ACCOUNT_ADDR, deleteAccountHandler),
            (CLICK_THOUGH_ADDR, clickThoughHandler)
        ],
        settings={
            'debug': True,
            'autoreload': True
        }
    )

    tornado.autoreload.start()
    
    the_port = PORT
    print('listen on port: %d'%the_port)
    
    application.listen(the_port)
    instance = tornado.ioloop.IOLoop.instance()
    instance.start()







