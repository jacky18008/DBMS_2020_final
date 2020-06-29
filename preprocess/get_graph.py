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

with open("ui.graph","w") as f:
    for data in rating_list:
        if int(data[2])>=3:
            f.write("[user]"+data[0]+"\t[item]"+data[1]+"\t1.000000\n")

entity_dict = {}
with open("./ml-1m/original_mapping.tsv","r") as f:
    for line in f:
        line = line.split()
        if (len(line) == 2):
            movie_id = line[0]
            entity_id = line[-1]
            entity_dict[line[-1]] = line[0]
        else:
            print(line)

kg_list = []
entity_list = []
with open("./ml-1m/kg.dat","r") as f:
    for line in f:
        line = line.split()
        if (len(line) == 3):
            entity_1 = line[0]
            entity_2 = line[1]
            relation = line[2]
            kg_list.append(line)
            entity_list.append(entity_1)
            entity_list.append(entity_2)
        else:
            print(line)

entity_list = list(set(entity_list))
with open("./ml-1m/new_mapping.dat","w") as f:
    i=1
    max_movie_id = 3952
    for entity in entity_list:
        if entity in entity_dict.keys():
            f.write(entity+" "+entity_dict[entity]+"\n")
        else:
            f.write(entity+" "+str(max_movie_id+i)+"\n")
            i = i+1
            entity_dict[entity] = str(max_movie_id+i)

r_dict = {}
with open("./ml-1m/r_map.dat","r") as f:
    for line in f:
        line = line.split()
        if (len(line) == 2):
            r_num = line[0]
            r_name = line[1].split("/")[-1]
            r_dict[r_num] = r_name
        else:
            print(line)

with open("iw.graph","w") as f:
    for kg in kg_list:
        entity_1 = entity_dict[kg[0]]
        entity_2 = entity_dict[kg[1]]
        relation = r_dict[kg[2]]
        f.write("[item]"+entity_1+"\t["+relation+"]"+entity_2+"\t1.000000\n")
