import json
with open("book.txt", "r") as f:
    for line in f.readlines():
        #print(json.loads(line).get(nid))
        print(json.loads(line)['nid'])
        if json.loads(line)['nid'] == "11":
            print("ok")
