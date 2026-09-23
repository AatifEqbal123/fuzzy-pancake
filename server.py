import json

for i in range(0, 4):
    rf = open(f"s{i}.json", "r")
    data = rf.readline()
    nd = json.loads(data)
    file_path = "/storage/emulated/0/P.F.S.S.S/reciever/Recieve_rough.json"
    
    with open(file_path, "a") as sf:
        json.dump(nd, sf)