import sqlite3
import hashlib
from datetime import datetime

def hash_function(account, password):
    plain_text = str(account) + str(password)
    hash_text =  hashlib.md5(plain_text.encode('latin1')).hexdigest()
    return hash_text

def get_timestamp():
    now = datetime.now()
    dt_string = now.strftime("%Y%m%d%H%M")
    return dt_string

def start_sql_connection():
    conn = sqlite3.connect('db.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
    return conn



PIC_URL_SAMPLE =    r"https://m.media-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg"
SEARCH_LIST_SAMPLE = [
    {
        'id':       "123",
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
        'id':       "122",
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
        'id':       "12312",
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
        'id':       "12223",
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
        'id':       "123123223",
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
        'id':       "12222222223",
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
        'id':       "12114523",
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
        'id':       "128383",
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
        'id':       "12392929",
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
        'id':       "123010101",
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
        'id':       "1232",
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
        'id':       "123",
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
        'id':       "1231000",
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
        'id':       "1230",
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
        'id':       "123000000",
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
        'id':       "12301010",
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
        'id':       "123736663",
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
        'id':       "12366699",
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
        'id':       "12327",
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
        'id':       "123767",
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
        'id':       "123890",
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
        'id':       "12443",
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
        'id':       "12279453",
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
        'id':       "123009",
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
        'id':       "12390909909090",
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

