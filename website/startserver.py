import tornado.web
import tornado.ioloop
import tornado.autoreload
import requests as req
import json
import hashlib
import os
from datetime import datetime

API_ADDRESS = "http://127.0.0.1:8888"
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
                        'desciprtion': xxxxxxxx,
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

# functional group
def hash_function(account, password):
    plain_text = str(account) + str(password)
    hash_text =  hashlib.md5(plain_text.encode('latin1')).hexdigest()
    return hash_text

def watch_directories(dirs):
    watchlist = []
    for d in dirs:
        for f in os.listdir(d):
            if '.html' in f or '.py' in f or '.js' in f or '.css' in f:
                watchlist.append(os.path.join(d,f))
    for p in watchlist:
        full_path = os.path.abspath(p)
        print(full_path)
        tornado.autoreload.watch(os.path.abspath(p))

def get_timestamp():
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M")
    return dt_string



# view group
class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", TIMESTAMP=get_timestamp())

    def post(self):
        myhash = self.get_argument('hash', None)
        if myhash:
            res = req.post(HASH_VALIDATE_ADDR, {'hash':myhash})
            res_json = json.loads(res.content)
            if res_json['status'] == 'valid':
                self.render("dashboard.html", NAME=res_json['name'], HASH=myhash, TIMESTAMP=get_timestamp())
        else:
            self.render("index.html", TIMESTAMP=get_timestamp())
        
class editHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", TIMESTAMP=get_timestamp())

    def post(self):
        myhash = self.get_argument('hash', None)
        if myhash:
            res = req.post(HASH_VALIDATE_ADDR, {'hash':myhash})
            res_json = json.loads(res.content)
            if res_json['status'] == 'valid':
                res = req.post(PERSONAL_INFO_ADDR, {'hash':myhash})
                res_json = json.loads(res.content)
                name = res_json['name']
                account = res_json['account']
                gender = res_json['gender']
                if gender == 'M':
                    _m, _f = 'checked', ''
                elif gender == 'F':
                    _m, _f = '', 'checked'
                self.render("edit.html", HASH=myhash, NAME=name, ACCOUNT=account, is_male=_m, is_female=_f)
        else:
            self.render("index.html", TIMESTAMP=get_timestamp())

class loginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        account = self.get_argument('account', None)
        password = self.get_argument('password', None)
        myhash = hash_function(account, password)
        print("md5(%s%s)=%s"%(account, password, myhash))
        res = req.post(HASH_VALIDATE_ADDR, {'hash':myhash})
        res_json = json.loads(res.content)
        message = {'status': res_json['status']}
        self.write(json.dumps(message))

class registerHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")



if __name__ == "__main__":
    application = tornado.web.Application([
            (r"/", indexHandler),
            (r"/edit", editHandler),
            (r"/login", loginHandler),
            (r"/register", registerHandler),

            (r'/js/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/js'}),
            (r'/css/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/css'}),
            (r'/img/(.*)', tornado.web.StaticFileHandler, {'path': 'assets/img'})
        ],
        settings={
            'debug': True,
            'autoreload': True
        }
    )

    watchdirs = [
        'assets/css',
        'assets/js',
        'widget',
        '.'
    ]
    tornado.autoreload.start()
    watch_directories(watchdirs)
    
    the_port = 8889
    print('listen on port: %d'%the_port)
    
    application.listen(the_port)
    instance = tornado.ioloop.IOLoop.instance()
    instance.start()