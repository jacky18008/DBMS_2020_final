import os, sys

L = "'http://"
R = ":8888"

def ip_replacer(fpath, new_ip, Ld, Rd):
    new_content = ""

    with open(fpath, 'r', encoding='utf8') as f:
        all_content = f.read()
        print("file:\t\t%s"%fpath)

        ip_left = all_content.find(Ld)
        while ip_left != -1:
            part_A = all_content[:ip_left]
            part_B = all_content[ip_left+len(Ld):]

            ip_right = part_B.find(Rd)
            if ip_right == -1:
                break
            else:
                curr_ip = part_B[:ip_right]
                part_B = part_B[ip_right:]

            new_content += part_A + Ld + new_ip + Rd

            print("current ip:\t%s"%curr_ip)
            print("new ip:\t\t%s"%new_ip)
            
            all_content = part_B[len(Rd):]
            ip_left = all_content.find(Ld)
        new_content += all_content
    
    with open(fpath, 'w', encoding='utf8') as f:
        f.write(new_content)

files = ["dashboard.html", "register.html", "edit.html", "assets/js/api_search.js"]

for fname in files:
    ip_replacer(fname, sys.argv[1], L, R)
    print()
