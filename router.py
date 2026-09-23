#reading data and diving it into 4 temp_es
import random
import json
import textwrap

f = open("inbox.py", "r")
data = f.readline()
holder = ""
hsh_list= []

x = 0
for i in data:
    if(x == 0 or x%3 == 0):
        x += 1
        continue
        
    if(len(holder) == 2):
        hsh_list.append(holder)
        holder = ""
        
    holder += i
    x += 1
 

if holder:
    hsh_list.append(holder)

random.shuffle(hsh_list)
random.shuffle(hsh_list)
random.shuffle(hsh_list)
random.shuffle(hsh_list)

print("data :", data, "\n")       
print("hsh_list:", hsh_list)

# dividing into 4 temp_es

new_list = []
hold = ""

for i in hsh_list:
    
    if(len(hold) == 16):
        new_list.append(hold)
        hold = ""
        
    hold += i

if hold:
            new_list.append(hold)   
            
print("new_list :", new_list)

temp_1 = [new_list[0]]
temp_2 = [new_list[1]]
temp_3 = [new_list[2]]
temp_4 = [new_list[3]]

print("\n", temp_1, temp_2, temp_3, temp_4)

# Swapping characters

def swap(a):
    str = a[0]
    return "".join(random.sample(str, len(str)))
    
Crate_1 = [swap(temp_1)]
Crate_2 = [swap(temp_2)]
Crate_3 = [swap(temp_3)]
Crate_4 = [swap(temp_4)]

print(Crate_1, Crate_2, Crate_3, Crate_4)

# Swapping across lists

def sl(A, B):
    str = A[0] + B[0]
    rndm = "".join(random.sample(str, len(str)))
    print(rndm)
    mp = len(rndm) // 2
    str1 = rndm[:mp]
    str2 = rndm[mp:]

    l1, l2 = [str1], [str2]
    return l1, l2

Box1, Box2 = sl(Crate_1, Crate_2)
Box3, Box4 = sl(Crate_3, Crate_4)
print("\n", Box1, Box2, Box3, Box4) 

random.shuffle(Box1)
random.shuffle(Box2)
random.shuffle(Box3)
random.shuffle(Box4)

mn =[]
mn.append(Box1)
mn.append(Box2)
mn.append(Box3)
mn.append(Box4)

#Making collector id
a = 0
b = 0
code = ""
STR = "".join(hsh_list)
sstr = "".join(Box1 + Box2 + Box3 + Box4)

for i in range(0, len(STR)):
    for x in range(0, len(STR)):
        if(b >= len(STR)):
                break
                
        elif(a >= len(STR)):
            a = 0
            b += 1
          
        elif(str(a) in code):
            a += 1  
            
        elif(sstr[b] == STR[a] and str(a) not in  code):
            ta = str(a) + "_"
            code += ta
            b += 1
            a = 0
            
        elif(sstr[b] != STR[a]):
            a += 1
            
print("\n", STR)
print("\n", sstr)
print("\n", code)

TRI = "1245@#$_"    
lengthT = len(TRI) // 4

partsT = textwrap.wrap(TRI, lengthT)


class box_data:
    def __init__(self, list, codde, TRI):
        self.list = list
        self.codde = codde
        self.TRI = TRI

CL = code
length = len(CL) // 4

parts = textwrap.wrap(CL, length)
print("\n", parts)


shelf_1 = box_data(Box1, parts[0], partsT[0])
shelf_2 = box_data(Box2, parts[1], partsT[1])
shelf_3 = box_data(Box3, parts[2], partsT[2])
shelf_4 = box_data(Box1, parts[3], partsT[3])


          
print("\n", shelf_1.codde)
nmn = [shelf_1, shelf_2, shelf_3, shelf_4]

data1 = {"list" : shelf_1.list, "code" : shelf_1.codde, "TRI" : shelf_1.TRI}

data2 = {"list" : shelf_2.list, "code" : shelf_2.codde, "TRI" : shelf_2.TRI}

data3 = {"list" : shelf_3.list, "code" : shelf_3.codde, "TRI" : shelf_3.TRI}

data4 = {"list" : shelf_4.list, "code" : shelf_4.codde, "TRI" : shelf_4.TRI}

print("\n", sstr)
print("\n", STR)
print("\n", code)

# Sending data

x = 0
z = 1
for i in range(0, 4):
    
    s = "s" + str(i)
    
    
    sf = open(f"{s}.txt", "w")
    json.dump(f"data{z}", sf)
    x += 1
    z += 1
    sf.close()
    
print(shelf_1.list)

sf1 = open("s0.txt", "w")
json.dump(data1, sf1)
    
sf2 = open("s1.txt", "w")
json.dump(data2, sf2)
    
sf3 = open("s2.txt", "w")
json.dump(data3, sf3)
        
sf4 = open("s3.txt", "w")
json.dump(data4, sf4)

sf1.close()
sf2.close()
sf3.close()
sf4.close()