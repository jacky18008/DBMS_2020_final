
_API_ADDRESS = "" #"127.0.0.1:8888"

PORT = 8888

HASH_VALIDATE_ADDR = "%s/hash_validate"%_API_ADDRESS
'''
send:       {'hash': hash}
receive:    {'status': stat, 'name': username}
            stat:
                success=    "valid"
                failure=    "invalid"
'''
REGISTER_ADDR = "%s/register"%_API_ADDRESS
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
PERSONAL_INFO_ADDR = "%s/personal_info"%_API_ADDRESS
'''
send:       {'hash': hash}
receive:    {
                'name':     name,
                'account':  account,
                'gender':   gender
            }
'''
PERSONAL_INFO_UPDATE_ADDR = "%s/personal_info_update"%_API_ADDRESS
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
SEARCH_MOVIE_ADDR = "%s/search"%_API_ADDRESS
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
RECOMMEND_MOVIE_ADDR = "%s/recommend"%_API_ADDRESS
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
DELETE_ACCOUNT_ADDR = "%s/delete_account"%_API_ADDRESS
''' from js
send:       {'hash': hash, 'password': pwd}
receive:    {'status': stat, 'message': text}
            stat:
                success=    "valid"
                failure=    "invalid"
            text:
                password error= "password incorrect"
'''
CLICK_THOUGH_ADDR = "%s/clicked"%_API_ADDRESS
'''
send:       {'hash': hash, 'mid': movie_id}
receive:    full
'''