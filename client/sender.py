
print("hello world")

#Making chat files and updating

import hashlib
import random
import json

while True:
    ChatFile = open("chat.txt", "a+")
    ChatFile.seek(0)
    print(ChatFile.read())

    msg = input("enter your msg: ")
    
    ChatFile.write("\n" + msg)
    
    #Hashing the data
    
    h = hashlib.sha256()
    h.update(msg.encode("utf-8")) 
    
    hshmsg = h.hexdigest()
    hshlist = []
    i = 0
    li = 0
    Box = ""
    
    for i in range(0, 64) :
        Box += hshmsg[i]
        i += 1
        if(len(Box) == 2):
            hshlist.append(Box)
            Box = ""
            
    rndmlist = random.sample(hshlist, len(hshlist))
   
   
    # Sending message to server
    list = []
    
    for i in rndmlist:
        list.append(str(i))
     
    
    join = "_".join(list)
    val = "_" + join
    
    mnfile = open("../inbox.py", "a")
    mnfile.write(f'''{val}''')
    mnfile.close()
    #Sender mesaage screen reader
    
    ChatFile.seek(0)
    print(ChatFile.read())
    
    ChatFile.close()