import tornado.web
import tornado.ioloop
import tornado.autoreload
import requests as req
import json
import hashlib
import os
from datetime import datetime

API_ADDRESS = "" #"127.0.0.1:8888"
PORT = 8888
HASH_VALIDATE_ADDR = "%s/hash_validate"%API_ADDRESS
'''
send:       {'hash': hash}
receive:    {'status': stat, 'name': username}
            stat:
                success=    "valid"
                failure=    "invalid"
'''
REGISTER_ADDR = "%s/register"%API_ADDRESS
''' from js
send:       {
                'name':     name,
                'account':  account,
                'password': password,
                'gender':   gender,
            }
receive:    {'status': stat, 'message': text}
            stat:
                success=    "valid"
                failure=    "invalid"
            text (when stat is invalid):
                account repeated=   "account already existed!"
'''
PERSONAL_INFO_ADDR = "%s/personal_info"%API_ADDRESS
'''
send:       {'hash': hash}
receive:    {
                'name':     name,
                'account':  account,
                'gender':   gender
            }
'''
PERSONAL_INFO_UPDATE_ADDR = "%s/personal_info_update"%API_ADDRESS
''' from js
send:       {
                'hash':     hash,
                'name':     name,
                'password': password,
                'gender':   gender
            }
receive:    {'status': stat, 'message': text}
            stat:
                success=    "valid"
                failure=    "invalid"
            text:
                hash incorrect=     500 internal error
                password changed=   "re_login"
                other=              "..."
'''
SEARCH_MOVIE_ADDR = "%s/search"%API_ADDRESS
''' from js
send:       {'query': movie}
receive:    {
                results: [
                    {
                        'id':       ooo,
                        'name':     xxx,
                        'genres':   "xxx/xxx/xxx",
                        'director': xxx,
                        'company':  xxx,
                        'year':     oooo,
                        'actors':   "xxx,xxxx,xxx,xx",
                        'description': xxxxxxxx,
                        'img':      xoxoxoxo
                    },
                    ...
                ]
            }
'''
RECOMMEND_MOVIE_ADDR = "%s/recommend"%API_ADDRESS
''' from js
send:       {'hash': hash}
receive:    {
                results: [
                    {
                        'id':       ooo,
                        'name':     xxx,
                        'genres':   "xxx/xxx/xxx",
                        'director': xxx,
                        'company':  xxx,
                        'year':     oooo,
                        'actors':   "xxx,xxxx,xxx,xx",
                        'description': xxxxxxxx,
                        'img':      xoxoxoxo
                    },
                    ...
                ]
            }
'''
ADD_CLICKED_MOVIE_ADDR = "%s/clicked"%API_ADDRESS
''' from js
send:       {'hash': hash, 'id': id}
receive:    null
'''

PIC_URL_SAMPLE =    r"https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg"
HASH_SAMPLE =       r"c8837b23ff8aaa8a2dde915473ce0991"
ACCOUNT_SAMPLE =    r"123"
PASSWORD_SAMPLE =   r"321"
NAME_SAMPLE =       r"philip"
GENDER_SAMPLE =     r"M"
SEARCH_LIST_SAMPLE = [
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "BBB",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "BBB",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "BBB",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "BBB",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "BBB",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    }
]
REC_LIST_SAMPLE = [
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "CCC",
        'genres':   "Comedy/Family",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "DDD",
        'genres':   "",
        'director': "(N/A)",
        'company':  "(N/A)",
        'year':     "unknown",
        'actors':   "(N/A)",
        'description': "(N/A)",
        'img':      "http://www.baytownmotors.com/wp-content/uploads/2013/11/dummy-image-square.jpg"
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "CCC",
        'genres':   "Comedy/Family",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "DDD",
        'genres':   "",
        'director': "(N/A)",
        'company':  "(N/A)",
        'year':     "unknown",
        'actors':   "(N/A)",
        'description': "(N/A)",
        'img':      "http://www.baytownmotors.com/wp-content/uploads/2013/11/dummy-image-square.jpg"
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "CCC",
        'genres':   "Comedy/Family",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "DDD",
        'genres':   "",
        'director': "(N/A)",
        'company':  "(N/A)",
        'year':     "unknown",
        'actors':   "(N/A)",
        'description': "(N/A)",
        'img':      "http://www.baytownmotors.com/wp-content/uploads/2013/11/dummy-image-square.jpg"
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "CCC",
        'genres':   "Comedy/Family",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "DDD",
        'genres':   "",
        'director': "(N/A)",
        'company':  "(N/A)",
        'year':     "unknown",
        'actors':   "(N/A)",
        'description': "(N/A)",
        'img':      "http://www.baytownmotors.com/wp-content/uploads/2013/11/dummy-image-square.jpg"
    },
    {
        'name':     "AAA",
        'genres':   "Action/Romance",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1996",
        'actors':   "philip, amy, david",
        'description': "dfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "CCC",
        'genres':   "Comedy/Family",
        'director': "xxx",
        'company':  "yyy",
        'year':     "1997",
        'actors':   "amy, david",
        'description': "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdfdf",
        'img':      PIC_URL_SAMPLE
    },
    {
        'name':     "DDD",
        'genres':   "",
        'director': "(N/A)",
        'company':  "(N/A)",
        'year':     "unknown",
        'actors':   "(N/A)",
        'description': "(N/A)",
        'img':      "http://www.baytownmotors.com/wp-content/uploads/2013/11/dummy-image-square.jpg"
    }
]

# functional group
def hash_function(account, password):
    plain_text = str(account) + str(password)
    hash_text =  hashlib.md5(plain_text.encode('latin1')).hexdigest()
    return hash_text

def get_timestamp():
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M")
    return dt_string

class baseHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET')

class hashHandler(baseHandler):
    def post(self):
        global HASH_SAMPLE
        myhash = self.get_argument('hash', None)
        print(myhash)
        if myhash:
            if myhash == HASH_SAMPLE:
                message = {'status': "valid", 'name': 'Philip Wang'}
            else:
                message = {'status': "invalid"}
        else:
            message = {'status': "invalid"}

        self.write(json.dumps(message))
            
        
class regHandler(baseHandler):
    def post(self):
        global NAME_SAMPLE
        global ACCOUNT_SAMPLE
        global PASSWORD_SAMPLE
        global GENDER_SAMPLE
        global HASH_SAMPLE
        name = self.get_argument('name', None)
        account = self.get_argument('account', None)
        password = self.get_argument('password', None)
        gender = self.get_argument('gender', None)
        if name and account and password and gender:
            if account == ACCOUNT_SAMPLE:
                message = {'status': "invalid", 'message': "account is already existed!"}
            else:
                HASH_SAMPLE = hash_function(account, password)
                NAME_SAMPLE = name
                ACCOUNT_SAMPLE = account
                PASSWORD_SAMPLE = password
                GENDER_SAMPLE = gender
                message = {'status': "invalid"}
            self.write(json.dumps(message))
        else:
            self.set_status(400)

class infoHandler(baseHandler):
    def post(self):
        global NAME_SAMPLE
        global ACCOUNT_SAMPLE
        global PASSWORD_SAMPLE
        global GENDER_SAMPLE
        global HASH_SAMPLE
        myhash = self.get_argument('hash', None)
        if myhash:
            if myhash == HASH_SAMPLE:
                message = {'name': NAME_SAMPLE, 'account': ACCOUNT_SAMPLE, 'gender': GENDER_SAMPLE}
                self.write(json.dumps(message))
            else:
                self.set_status(400)
        else:
            self.set_status(400)

class infoUpdateHandler(baseHandler):
    def post(self):
        global NAME_SAMPLE
        global PASSWORD_SAMPLE
        global GENDER_SAMPLE
        global HASH_SAMPLE
        myhash = self.get_argument('hash', None)
        if myhash:
            if myhash == HASH_SAMPLE:
                message = {'status': 'valid'}
                new_name = self.get_argument('name', None)
                NAME_SAMPLE = new_name if new_name else NAME_SAMPLE
                new_gender = self.get_argument('gender', None)
                GENDER_SAMPLE = new_gender if new_gender else GENDER_SAMPLE
                new_password = self.get_argument('password', None)
                message['message'] = "Personal Info updated Successfully!"
                if new_password != "" and new_password != None:
                    PASSWORD_SAMPLE = new_password
                    global ACCOUNT_SAMPLE
                    new_hash = hash_function(ACCOUNT_SAMPLE, PASSWORD_SAMPLE)
                    HASH_SAMPLE = new_hash
                    message['message'] = "re_login"
                self.write(json.dumps(message))
            else:
                self.set_status(400)
        else:
            self.set_status(400)

class searchHandler(baseHandler):
    def post(self):
        message = {'results': SEARCH_LIST_SAMPLE}
        self.write(json.dumps(message))

class recHandler(baseHandler):
    def post(self):
        message = {'results': REC_LIST_SAMPLE}
        self.write(json.dumps(message))
        

if __name__ == "__main__":
    application = tornado.web.Application([
            (HASH_VALIDATE_ADDR, hashHandler),
            (REGISTER_ADDR, regHandler),
            (PERSONAL_INFO_ADDR, infoHandler),
            (PERSONAL_INFO_UPDATE_ADDR, infoUpdateHandler),
            (SEARCH_MOVIE_ADDR, searchHandler),
            (RECOMMEND_MOVIE_ADDR, recHandler)
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