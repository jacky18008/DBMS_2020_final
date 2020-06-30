# DBMS 2020 final project

### Team Info
- Name: **CCLab**
- Members: [盧佳妤 LuJiaYu](https://github.com/lujiayu0807), [段寶鈞 Ivy](https://github.com/ivy753116), [陳先灝 Jacky](https://github.com/jacky18008), [王均捷 Rainboltz](https://github.com/rainboltz), [方文忠 LittleCube](https://github.com/littlecube2019)

---

## Database Preparations

- We created a database based on the public dataset [MovieLens-1M](https://grouplens.org/datasets/movielens/1m/)
- Instead of the public data, we also retreive some additional informations from websites by using the web crawlers.
- for reviewing the dataset on PostgresDB, we provide alternative raw data input using [SQL file](https://drive.google.com/open?id=15H_NnfM33FYJO-HLSnuzr-a3msspqZ8d) to import  dataset into the PostgresDB (**NOT RECOMMENDED**)
    ```bash
    psql -f "ml1m" -U username
    ```

### 1. crawl the additional informations

- the presentation can be previewed [here](https://nbviewer.jupyter.org/github/jacky18008/DBMS_2020_final/blob/master/crawler/IMDB_crawler.ipynb)
- we crawled the additional informations such as:
    1. movie poster
    2. directors
    3. writers
    4. stars
    5. introductions & storylines

### 2. dataset preprocess

- we remain the full dataset in our github repo [here](https://github.com/jacky18008/DBMS_2020_final/tree/master/preprocess) :)
- usage:
    ```bash
    cd preprocess
    python get_csv.py && get_graph.py
    ```

### 3. setup the database
1. download data from [google drive link](https://drive.google.com/file/d/13boe5aTZVV-pabHJv5Bw0AG5ykX1t9dk/view?fbclid=IwAR0lIPDRbNCsHleasjLq3tc9fTh-UrUJQrbMYDmH4Gi9TmGQZxbKytDaaE0)
2. its a `.sqlite` file, just put it under directory `sql_api_server`

---

## Website Service Instructions
- A pure handmade [MVC-structured](https://zh.wikipedia.org/zh-tw/MVC) website. Tornado on Python provides the **Controller**, the web pages are Templates (**Views**), and the SQL-api server infers to **Model**.
- Frontend is composed of [Bootstrap](https://getbootstrap.com/) + [jQuery](https://jquery.com/) (`#javascript`).
- Backend is provided by [Tornado](https://www.tornadoweb.org/en/stable/) (`#python`)
- SQL queries are safe and cannot be SQL injected :)

### 0. install requirements
- python version >= 3.6
- tornado >= 6.0.0
```bash
pip3 install -r requirements.txt
```

### 1. setup web service
- for windows, simply click `website_server/start.bat`.
- for general OS systems:
    ```bash
    cd website_server
    python startserver.py
    ```
- the website URL is default at [http://127.0.0.1:8889](http://127.0.0.1:8889).
- To change service IP address (default=`localhost`):
    ```bash
    cd website_server
    python set_server_ip.py 123.456.789.012
    ```
    then the website will be on `http://123.456.789.012:8889`

### 2. setup SQL-api service
- for windows, simply click `sql_api_server/start.bat`.
- for general OS systems:
    ```bash
    cd sql_api_server
    python correct_md5.py && startserver.py
    ```
- notice that this sql api service can be only used on localhost for security issues. (http://127.0.0.1:8888)
