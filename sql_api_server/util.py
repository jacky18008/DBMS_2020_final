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


def search(conn, query, total_each=8, total=16):
    result_id = set()

    title_results = []
    for cursor in list(conn.execute(f'''
                                    SELECT * 
                                    FROM movie
                                    WHERE movie.title like "%{query}%" limit {total_each}
                                ''')):
        result_id.add(cursor[0])
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp;%s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        title_results.append(this_result)
    for _ in range(len(title_results) - total_each):
        title_results.append(None)

    desc_results = []
    for cursor in list(conn.execute(f'''
                                    SELECT * 
                                    FROM movie
                                    WHERE movie.storyline like "%{query}%" limit {total_each}
                                ''')):
        if cursor[0] in result_id:
            continue
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp;%s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        desc_results.append(this_result)
    for _ in range(len(desc_results) - total_each):
        desc_results.append(None)

    type_results = []
    for _cursor in list(conn.execute(f'''
                                    SELECT * 
                                    FROM type
                                    WHERE type like "%{query}%" limit {total_each}
                                ''')):
        if _cursor[0] in result_id:
            continue
        result_id.add(_cursor[0])

        cursor = list(conn.execute('SELECT * FROM movie WHERE movie_id = ?', (_cursor[0],)))[0]
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp; %s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        type_results.append(this_result)
    for _ in range(len(type_results) - total_each):
        type_results.append(None)

    company_results = []
    for _cursor in list(conn.execute(f'''
                                    SELECT * 
                                    FROM company
                                    WHERE production_company like "%{query}%" limit {total_each}
                                ''')):
        if _cursor[0] in result_id:
            continue
        result_id.add(_cursor[0])
        cursor = list(conn.execute('SELECT * FROM movie WHERE movie_id = ?', (_cursor[0],)))[0]
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp; %s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        company_results.append(this_result)
    for _ in range(len(company_results) - total_each):
        company_results.append(None)

    
    #rerank
    output_results = \
        title_results[:2] + \
        desc_results[:2] + \
        type_results[:2] + \
        company_results[:2] + \
        title_results[2:4] + \
        desc_results[2:4] + \
        type_results[2:4] + \
        company_results[2:4] + \
        title_results[4:6] + \
        desc_results[4:6] + \
        type_results[4:6] + \
        company_results[4:6] + \
        title_results[6:] + \
        desc_results[6:] + \
        type_results[6:] + \
        company_results[6:]
    try:
        while True:
            output_results.remove(None)
    except:
        if len(output_results) > total:
            output_results = output_results[:total]
        return output_results


def recommend(conn, user_hash, total_each=6):
    user_id = list(conn.execute('select user_id from user where md5=?',(user_hash,)))[0][0]
    
    recs = []
    for cursor in list(conn.execute('''
                            SELECT DISTINCT movie.*
                            FROM model, movie
                            WHERE model.user_id=?
                            AND model.movie_id=movie.movie_id limit ?
                        ''', (user_id, total_each))):
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp; %s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        recs.append(this_result)
    
    for cursor in list(conn.execute('''
                SELECT DISTINCT movie.*
                FROM click, director AS adirector, director AS bdirector, movie
                WHERE click.user_id=?
                AND click.movie_id=adirector.movie_id
                AND adirector.director=bdirector.director
                AND movie.movie_id=bdirector.movie_id
                GROUP BY bdirector.movie_id
                ORDER BY MAX(click.click) DESC
                LIMIT ?
            ''', (user_id, total_each))):
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp; %s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        recs.append(this_result)

    for curaor in list(conn.execute('''
                SELECT DISTINCT movie.*
                FROM click, actor AS aactor, actor AS bactor, movie
                WHERE click.user_id=?
                AND click.movie_id=aactor.movie_id
                AND aactor.actor_actress=bactor.actor_actress
                AND movie.movie_id=bactor.movie_id
                GROUP BY bactor.movie_id
                ORDER BY MAX(click.click) DESC
                LIMIT ?
            ''', (user_id, total_each))):
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp; %s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        recs.append(this_result)
        
    return recs


def cold_recommend(conn):
    mids = ['999', '998', '997', '996', '994', '993', '992', '991', '990', '99']
    results = []
    for mid in mids:
        cursor = list(conn.execute('SELECT * FROM movie WHERE movie.movie_id = ?', (mid,)))[0]
        try:
            genres = '/'.join([ c[0] for c in conn.execute("select type from type where movie_id=?",(cursor[0],)) ])
        except:
            genres = '(N/A)'
        try:
            director = list(conn.execute("select director from director where movie_id=?",(cursor[0],)))[0][0]
        except:
            director = '(N/A)'
        try:
            company = list(conn.execute("select company from company where movie_id=?",(cursor[0],)))[0][0]
        except:
            company = '(N/A)'
        try:
            actors = ', '.join([ c[0] for c in conn.execute("select actor_actress from actor where movie_id=?",(cursor[0],)) ])
        except:
            actors = '(N/A)'
        this_result = {
            'id':       cursor[0],
            'name':     cursor[2],
            'genres':   genres,
            'director': director,
            'company':  company,
            'year':     str(cursor[1]),
            'actors':   actors,
            'description': "<i>“%s”</i>&nbsp;&nbsp;%s"%(cursor[5], cursor[4]),
            'img': cursor[6]
        }
        results.append(this_result)
    return results



