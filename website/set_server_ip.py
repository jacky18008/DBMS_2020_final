import os, sys

L = "'http://"
R = ":"

def ip_replacer(fpath, new_ip, Ld, Rd):
    new_content = ""

    with open(fpath) as f:
        all_content = f.read()

        part_A, part_B = all_content.split(Ld)
        part_A = part_A + Ld

        curr_IP, part_B = part_B.aplit(Rd)
        part_B = Rd + part_B

        print("file:\t\t\t%s"%fpath)
        print("current ip:\t%s"%curr_IP)
        print("new ip:\t\t%s"%new_ip)

        new_content = part_A + new_ip + part_B

    with open(fpath, 'w') as f:
        fpath.write(new_content)

files = ["dashboard.html", "register.html", "edit.html", "assets/js/api_search.js"]

for fname in files:
    ip_replacer(fname, sys.argv[1], L, R)
    print()
