import os
import csv
from random import randrange

database_folder = "./IMDB/"
movie_folders = os.listdir(database_folder)

# Preprocess: combine IMDB & ml1m datasets
movies_dict = {}
for i in range(len(movie_folders)):
    datas = os.listdir(database_folder+movie_folders[i])

    movie_dict = {"director": [], "rating": [], "star": [], "storyline": [], "summary_text": [], "writer": [], "production_co": [], "imgurl": []}
    for data in datas:
        if data == "movie_name":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                for line in f:
                    title = line.strip()
        if data == "director":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["director"] = [line.rstrip('\n') for line in f]
        if data == "rating":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["rating"] = [line.rstrip('\n') for line in f]
        if data == "star":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["star"] = [line.rstrip('\n') for line in f]
        if data == "storyline":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["storyline"] = [line.rstrip('\n') for line in f]
        if data == "summary_text":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["summary_text"] = [line.rstrip('\n') for line in f]
        if data == "writer":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["writer"] = [line.rstrip('\n') for line in f]
        if data == "production_co":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["production_co"] = [line.rstrip('\n') for line in f]
        if data == "imgurl":
            with open(database_folder+movie_folders[i]+"/"+data,"r",encoding="utf-8",errors="ignore") as f:
                movie_dict["imgurl"] = [line.rstrip('\n') for line in f]

    movies_dict[title] = movie_dict

ml1m_dict = {}
with open("./ml-1m/movies.dat","r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        movie_dict = {}
        line = line.strip().split("::")
        id = line[0]
        title = line[1].split(" (")[0]
        year = line[1].split()[-1][1:-1]
        type = line[-1]
        movie_dict["id"] = id
        movie_dict["year"] = year
        movie_dict["type"] = type
        ml1m_dict[title] = movie_dict

id_dict = {}
title_dict = {}

for title in movies_dict.keys():
    if title in ml1m_dict.keys():
        id_dict[ml1m_dict[title]["id"]] = title
        title_dict[title] = ml1m_dict[title]["id"]
    else:
        print(title)

# with open("title2id.data","w",encoding="utf-8") as f:
#     f.write("id\ttitle\n")
#     for id in id_dict.keys():
#         f.write(id+"\t"+id_dict[id]+"\n")

users_dict = {}
with open("./ml-1m/users.dat","r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        user_dict = {}
        line = line.strip().split("::")
        if (len(line) == 5):
            id = line[0]
            gender = line[1]
            age = line[2]
            occupation = line[3]
            zip_code = line[4]
            user_dict["gender"] = gender
            user_dict["age"] = age
            user_dict["occupation"] = occupation
            user_dict["zip_code"] = zip_code
            users_dict[id] = user_dict
        else:
            print(line)

rating_list = []
with open("./ml-1m/ratings.dat","r",encoding="utf-8",errors="ignore") as f:
    for line in f:
        rating_dict = {}
        line = line.strip().split("::")
        if (len(line) == 4):
            user_id = line[0]
            movie_id = line[1]
            rating = line[2]
            rating_list.append(line[0:-1])
        else:
            print(line)


# Get csv file
with open("movie.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["movie_id", "year", "title", "rating", "storyline", "summary_text", "imgurl"])
    for title in movies_dict.keys():
        if(movies_dict[title]["rating"] == []):
            rating = ""
        else:
            rating = movies_dict[title]["rating"][0]
        if(movies_dict[title]["storyline"] == []):
            storyline = ""
        else:
            storyline = movies_dict[title]["storyline"][0]
        if(movies_dict[title]["summary_text"] == []):
            summary_text = ""
        else:
            summary_text = movies_dict[title]["summary_text"][0]
        if(movies_dict[title]["imgurl"] == []):
            imgurl = ""
        else:
            imgurl = movies_dict[title]["imgurl"][0]
        writer.writerow([title_dict[title], ml1m_dict[title]["year"], title, rating, storyline, summary_text, imgurl])

with open("director.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["movie_id", "director"])
    for title in movies_dict.keys():
        movies_dict[title]["director"] = list(set(movies_dict[title]["director"]))
        for director in movies_dict[title]["director"]:
            writer.writerow([title_dict[title], director])

with open("screenwriter.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["movie_id", "screenwriter"])
    for title in movies_dict.keys():
        movies_dict[title]["writer"] = list(set(movies_dict[title]["writer"]))
        for screenwriter in movies_dict[title]["writer"]:
            writer.writerow([title_dict[title], screenwriter])

with open("actor.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["movie_id", "actor/actress"])
    for title in movies_dict.keys():
        movies_dict[title]["star"] = list(set(movies_dict[title]["star"]))
        for star in movies_dict[title]["star"]:
            writer.writerow([title_dict[title], star])

with open("company.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["movie_id", "production_company"])
    for title in movies_dict.keys():
        movies_dict[title]["production_co"] = list(set(movies_dict[title]["production_co"]))
        for production_co in movies_dict[title]["production_co"]:
            writer.writerow([title_dict[title], production_co])

with open("type.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["movie_id", "type"])
    for title in movies_dict.keys():
        movie_id = title_dict[title]
        types = ml1m_dict[title]["type"]
        types = types.strip().split("|")
        for type in types:
            writer.writerow([movie_id, type])

with open("click.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["user_id", "movie_id", "rating", "click"])
    for data in rating_list:
        movie_id = data[1]
        if movie_id in id_dict.keys():
            writer.writerow([data[0], data[1], data[2], randrange(1000)])

name_list = []
with open("actor.csv", newline='') as csvfile:
    lines = csv.reader(csvfile, delimiter='\t')
    for line in lines:
        name_list.append(line[1])
    name_list = list(set(name_list))

with open("director.csv", newline='') as csvfile:
    lines = csv.reader(csvfile, delimiter='\t')
    for line in lines:
        name_list.append(line[1])
    name_list = list(set(name_list))

with open("user.csv","w",encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(["user_id", "name", "account", "password", "gender", "age", "occupation", "zip_code"])
    for i, user_id in enumerate(users_dict.keys()):
        account = name_list[i].split()[0]+str(randrange(100,1000))
        password = name_list[i][0]+str(randrange(1000,10000))
        writer.writerow([user_id, name_list[i], account, password, users_dict[user_id]["gender"], users_dict[user_id]["age"], users_dict[user_id]["occupation"], users_dict[user_id]["zip_code"]])
