import json
import textwrap
import itertools

# Importing and checking "TRI"

# my_RI means register id that is given to every user and unique like ip adress

my_RI = "1245@#$_" 

file_path = "Recieve_rough.json"

with open(file_path, "r") as rf:
    whole_data = rf.read()
    
    length = len(whole_data) // 4
    
    parts = list(itertools.batched(whole_data, length))
    
    temp_1 = "".join(parts[0])
    temp_2 = "".join(parts[1])
    temp_3 = "".join(parts[2])
    temp_4 = "".join(parts[3])
    print(parts, "\n")   
    print(temp_1, "\n")
    print(len(temp_1))
    
    holder_1 = json.loads(temp_1)
    holder_2 = json.loads(temp_2)
    holder_3 = json.loads(temp_3)
    holder_4 = json.loads(temp_4)
    
    
    msg_TRI = "" 
    msg_TRI += (holder_1["TRI"])
    msg_TRI += (holder_2["TRI"])
    msg_TRI += (holder_3["TRI"])
    msg_TRI += (holder_4["TRI"])
    print(msg_TRI)
    
    if(msg_TRI == my_RI):
       print("\n", "TRI matched, verification level completed, sending to next level")

# Merging the list for random hash               
msg_list = ""
msg_list += "".join((holder_1["list"]))
msg_list += "".join((holder_2["list"]))
msg_list += "".join((holder_3["list"]))
msg_list += "".join((holder_4["list"]))

print("/n", msg_list)

# merging the code

msg_code = ""
msg_code += (holder_1["code"])
msg_code += (holder_2["code"])
msg_code += (holder_3["code"])
msg_code += (holder_4["code"])
print("\n", msg_code)
print("\n", msg_code[0])

# making original hash

'''
My code doesn't work

l = "0" * 64
nl = list(l)
x = ""
i = 0

for i in range(0, len(msg_code)):
    if(msg_code[i] != "_"):
        x += msg_code[i]
        i += 1
    
    elif(msg_code[i] == "_"):
        i += 1
        z = int(x)
        nl[z] = msg_code[z]
        x = ""

snl = "".join(nl)
print("\n", nl)              
print(snl)'''

positions = [int(p) for p in msg_code.split("_") if p]

shuffled_hash = msg_list
nl = [""] * 64

for char, original_index in zip(shuffled_hash, positions):
    nl[original_index] = char
    
original_hash = "".join(nl)
print(original_hash)

# Converting hash to message