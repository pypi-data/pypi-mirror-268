__version__=0.21
def info():
    print("CodeTool",str(__version__))
carac_id=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","#","è","ç","à","@","+","=","ê","ë","$","£","%","ù","µ","*",]
carac_code=carac_code=['8', 'B', 'h', 'o', 'ê', 'M', '[', 'z', '#', 'G', '1', 'Y', 'ç', 'n', 'à', 'D', '{', '~', 'u', 'X', '}', 'i', 'g', 'K', 'Z', ':', '!', '=', '.', '7', '&', '"', '4', 'x', '\\', '0', 'p', '?', '°', '$', 'W', 'E', 'H', ';', 'a', 'ë', 'w', 'y', '5', 'A', 'q', 'r', 'd', '*', 'U', 'I', 'J', '_', '§', '^', '%', 'S', 't', ')', ',', 'b', '3', ' ', 'j', ']', '+', 'é', 'C', 'R', '/', 'P', '6', 'm', 'v', '£', 'V', 'c', 'N', 'è', 'µ', 's', 'L', 'l', '2', 'f', '-', 'Q', 'ù', 'O', 'F', '(', 'k', '9', 'e', 'T', '@']
class CeasarCode:
    def __init__(self,key,liste):
        self.key = key
        self.liste = liste
    def encrypt(self,text):
        encrypted_text=''
        for char in text:
            if char in self.liste:
                shifted_index=(self.liste.index(char) + self.key) % len(self.liste)
                encrypted_text += self.liste[shifted_index]
            else:
                encrypted_text += char
        return encrypted_text
    def decrypt(self,text):
        decrypted_text=''
        for char in text:
            if char in self.liste:
                shifted_index = (self.liste.index(char) - self.key) % len(self.liste)
                decrypted_text += self.liste[shifted_index]
            else:
                decrypted_text += char
        return decrypted_text
class KeyLenghtError(Exception):
    pass
class LenghtError(Exception):
    pass
import random,datetime,time
def mix(lenght=30):
    random.shuffle(carac_id)
    if not type(lenght)==int:
        raise TypeError("Lenght must be a int.")
    start="" 
    for i in range(random.randint(lenght+1,lenght+284)):
        random.seed=int(i*3.1415)
        start=start+random.choice(carac_id)
    startt=start[0:lenght]
    try:
        endd=start[lenght+1::]
    except:
        pass
    if not len(endd)<=3:
        for i in range(len(endd)):
            startt[random.randint(0,lenght-1)]==endd[0]
            endd=endd[1::]
    start=startt
    return start
def universal_id1():
    time=str(datetime.datetime.now())
    syear=int(time[0:3])*31536000
    smonth=int(time[5:6])*2592000
    sday=int(time[8:9])*86400
    shour=int(time[11:12])*3600
    smin=int(time[14:15])*60
    second=int(time[17:18])
    time=str(syear+smonth+sday+shour+smin+second)[0:10]
    return time+"-"+mix(8)+"-"+mix(8)+"-"+mix(8)+"-"+mix(32)+"-1"
def generate_key():
    liste=[]
    while len(liste)!=100:
        for i in range(100):
            try:
                first=int(str(time.time()).split(".")[1][1:6])/int(str(time.time()).split(".")[0])
                time.sleep(first/5875875)
                first=str(first)[3:7]
                first=int(first)
                liste.append(first)
            except ValueError:
                pass
    random.seed(liste[66])
    random.shuffle(liste)
    for i in range(len(liste)):
        if len(str(liste[i]))==4:
            pass
        elif len(str(liste[i]))>4:
            liste[i]=int(str(liste[i])[0:5])
        elif len(str(liste[i]))<4:
            while not len(str(liste[i]))==4:
                liste[i]=int(str(liste[i])+str(random.randint(0,9)))
    return liste
def code(text:str,key:list=generate_key()):
    if not type(key)==list:
        raise TypeError("Key must be a list.")
    if not len(key)==100:
        raise KeyLenghtError("Key lenght must be 100.")
    if not type(text)==str:
        raise TypeError("Text to encode must be a string.")
    for i in key:
        if not type(i)==int:
            raise TypeError("All the number inside the key must integer.")
    for i in key:
        if not len(str(i))==4:
            raise LenghtError("One number isn't the required lenght.")
    schema=[]
    for i in range(len(key)):
        if str(key[i])[0] in ["1","6","8","9"]:
            schema.append("+")
        else:
            schema.append("-")
    move=0
    for o in range(len(schema[1::])):
        if schema[i]=="+":
            move=move+int(key[o])
        else:
            move=move-int(key[o])
    if str(move).startswith("-"):
        move=move*-1
    newtext=CeasarCode(move,carac_code).encrypt(text)
    return newtext
def decode(text:str,key:list):
    if not type(key)==list:
        raise TypeError("Key must be a list.")
    if not len(key)==100:
        raise KeyLenghtError("Key lenght must be 100.")
    if not type(text)==str:
        raise TypeError("Text to decode must be a string.")
    for i in key:
        if not type(i)==int:
            raise TypeError("All the number inside the key must integer.")
    for i in key:
        if not len(str(i))==4:
            raise LenghtError("One number isn't the required lenght.")
    schema=[]
    for i in range(len(key)):
        if str(key[i])[0] in ["1","6","8","9"]:
            schema.append("+")
        else:
            schema.append("-")
    move=0
    for o in range(len(schema[1::])):
        if schema[i]=="+":
            move=move+int(key[o])
        else:
            move=move-int(key[o])
    if str(move).startswith("-"):
        move=move*-1
    newtext=CeasarCode(move,carac_code).decrypt(text)
    return newtext
if __name__=="__main__":
    liste=['8', 'B', 'h', 'o', 'ê', 'M', '[', 'z', '#', 'G', '1', 'Y', 'ç', 'n', 'à', 'D', '{', '~', 'u', 'X', '}', 'i', 'g', 'K', 'Z', ':', '!', '=', '.', '7', '&', '"', '4', 'x', '\\', '0', 'p', '?', '°', '$', 'W', 'E', 'H', ';', 'a', 'ë', 'w', 'y', '5', 'A', 'q', 'r', 'd', '*', 'U', 'I', 'J', '_', '§', '^', '%', 'S', 't', ')', ',', 'b', '3', ' ', 'j', ']', '+', 'é', 'C', 'R', '/', 'P', '6', 'm', 'v', '£', 'V', 'c', 'N', 'è', 'µ', 's', 'L', 'l', '2', 'f', '-', 'Q', 'ù', 'O', 'F', '(', 'k', '9', 'e', 'T', '@']
    text=""
    import random
    for i in range(500):
        text=text+liste[random.randint(0,len(liste)-1)]
    print(universal_id1())

#Secure_id

import random
from random import sample
lettremin=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lettremaj=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
chiffre=["0","1","2","3","4","5","6","7","8","9"]
def secureid_sid1():
    ensemble=lettremin+lettremaj+chiffre
    random.shuffle(ensemble)
    boucle=int(random.choice(chiffre))
    for i in range(boucle):
        random.shuffle(ensemble)
    code=random.randint(1000,9999)
    result=str(code)
    certif=""
    for i in range(8):
        if random.randint(0,1)==1:
            certif+=str(random.choice(lettremaj))
        else:
            certif+=str(random.choice(lettremin))
    certiflong=certif*code
    lettre=certiflong[code]
    result+="-"+certif
    result+="-"+lettre
    court=""
    for i in range(3):
        court=""
        for i in range(4):
            court+=str(random.choice(ensemble))
        result+="-"+court
    longstr=""
    for i in range(24):
        longstr+=str(random.choice(ensemble))
    result+="-"+longstr
    result+="-1"
    return(result)
def secureid_sid2():
    ensemble=lettremin+lettremaj+chiffre
    random.shuffle(ensemble)
    boucle=int(random.choice(chiffre))
    for i in range(boucle):
        random.shuffle(ensemble)
    code=random.randint(100000,999999)
    result=str(code)
    certif=""
    for i in range(12):
        if random.randint(0,1)==1:
            certif+=str(random.choice(lettremaj))
        else:
            certif+=str(random.choice(lettremin))
    certiflong=certif*code
    lettre=certiflong[code]
    result+="-"+certif
    result+="-"+lettre
    court=""
    for i in range(3):
        court=""
        for i in range(4):
            court+=str(random.choice(ensemble))
        result+="-"+court
    longstr=""
    for i in range(24):
        longstr+=str(random.choice(ensemble))
    result+="-"+longstr
    result+="-2"
    return(result)

#Indecode

import random
from PIL import Image
import os
text="hello world"
carac=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"#","{","}","(",")","[","]","-","è","_","\\","ç","^","à","@","°","+","=","ê","ë","$","£","%","ù","µ","*",",","?",".",";",":","/","!","§"]
class IndecodeCodeError(Exception):
    pass
class IndecodeDecodeError(Exception):
    pass
class IndecodeKeyElementError(Exception):
    pass
class IndecodeKeyLengthError(Exception):
    pass
class IndecodeImageNotFoundError(Exception):
    pass
def indecode_generate_key(seed:int=None):
    if seed==None:
        carac=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"#","{","}","(",")","[","]","-","è","_","\\","ç","^","à","@","°","+","=","ê","ë","$","£","%","ù","µ","*",",","?",".",";",":","/","!","§"]
        random.shuffle(carac)
        key=""
        for i in range(len(carac)):
            key=key+carac[i]
        return key
    else:
        carac=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","&","é","~",'"',"#","{","}","(",")","[","]","-","è","_","\\","ç","^","à","@","°","+","=","ê","ë","$","£","%","ù","µ","*",",","?",".",";",":","/","!","§"]
        random.Random(seed).shuffle(carac)
        key=""
        for i in range(len(carac)):
            key=key+carac[i]
        return key
def indecode_code(text:str,key:str):
    newtext=""
    incode={}
    if not type(text)==str:
        raise TypeError("text argument must be a string")
    if not type(key)==str:
        raise TypeError("key argument must be a string")
    keylist=list(key)
    if not len(keylist)==len(carac):
        raise IndecodeKeyLengthError("the key is not of the expected length.")
    for i in range(len(keylist)):
        if not keylist[i] in carac:
            raise IndecodeKeyElementError("'"+keylist[i]+"' must not be in the key.")
    for i in range(len(key)):
        incode.update({carac[i]:key[i]})
    incode.update({" ":" "})
    incode.update({"'":"'"})
    for i in range(len(text)):
        if not text[i] in incode:
            raise IndecodeCodeError("'"+text[i]+"' is not encodable.")
        newtext=newtext+incode[text[i]]
    return newtext
def indecode_decode(text:str,key:str):
    newtext=""
    uncode={}
    if not type(text)==str:
        raise TypeError("text argument must be a string")
    if not type(key)==str:
        raise TypeError("key argument must be a string")
    keylist=list(key)
    if not len(keylist)==len(carac):
        raise IndecodeKeyLengthError("the key is not of the expected length.")
    for i in range(len(keylist)):
        if not keylist[i] in carac:
            raise IndecodeKeyElementError("'"+keylist[i]+"' must not be in the key.")
    for i in range(len(key)):
        uncode.update({key[i]:carac[i]})
    uncode.update({" ":" "})
    uncode.update({"'":"'"})
    for i in range(len(text)):
        if not text[i] in uncode:
            raise IndecodeDecodeError("'"+text[i]+"' is not decodable.")
        newtext=newtext+uncode[text[i]]
    return newtext
def indecode_get_key_with_img(image:str):
    if os.path.exists(image):
        img=Image.open(image)
        seed=int(img.width)/10*300+int(img.height)/20*600
        return indecode_generate_key(seed)
    else:
        raise IndecodeImageNotFoundError("'"+image+"' not found.")
    
#Hashint

hash_carac=['.', '~', '7', ']', 'z', '3', 'B', 'f', ':', 'R', '_', '+', 'é', '2', ',', 'ù', 'E', 'J', '°', 'F', 'i', '5', 'e', 'S', 'G', 'à', 'T', 'k', 'l', '§', '"', '0', 'I', '{', 'A', '/', 'K', '!', 'g', 'o', '?', '#', 'C', 'n', 'è', 'w', '*', ')', 'ë', 'V', 'D', 'H', '6', ' ', '^', 'ê', '-', 'd', ';', 'c', 't', 'U', 'v', '1', 'µ', 'Q', '8', 'm', '$', 'u', 'q', '[', '9', 'X', 'ç', 'a', '£', 'p', '=', 'M', 'h', 'W', '4', 'r', 'P', 's', 'Y', '%', 'N', '}', '(', '@', ',', 'y', 'Z', '&', 'L', 'x', 'O', '\\', 'b', 'j',"'"]
carat=""
class HashintError(Exception):
    pass
for i in range(len(hash_carac)):
    carat=carat+hash_carac[i]
def hash64(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+64)**64).endswith("0"):
                cara=str((hash_carac.index(text[i])+64)**64)[::str((hash_carac.index(text[i])+64)**64).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+64)**64)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash128(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+128)**128).endswith("0"):
                cara=str((hash_carac.index(text[i])+128)**128)[::str((hash_carac.index(text[i])+128)**128).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+128)**128)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash256(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+256)**256).endswith("0"):
                cara=str((hash_carac.index(text[i])+256)**256)[::str((hash_carac.index(text[i])+256)**256).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+256)**256)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash512(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+512)**512).endswith("0"):
                cara=str((hash_carac.index(text[i])+512)**512)[::str((hash_carac.index(text[i])+512)**512).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+512)**512)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash1024(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+1024)**1024).endswith("0"):
                cara=str((hash_carac.index(text[i])+1024)**1024)[::str((hash_carac.index(text[i])+1024)**1024).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+1024)**1024)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash2048(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+2048)**2048).endswith("0"):
                cara=str((hash_carac.index(text[i])+2048)**2048)[::str((hash_carac.index(text[i])+2048)**2048).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+2048)**2048)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash4096(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+4096)**4096).endswith("0"):
                cara=str((hash_carac.index(text[i])+4096)**4096)[::str((hash_carac.index(text[i])+4096)**4096).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+4096)**4096)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
def hash8192(text:str):
    if not type(text)==str:
        raise TypeError("text must be an str")
    newtext=""
    for i in range(len(text)):
        car=text[i]
        if car in hash_carac:
            if str((hash_carac.index(text[i])+8192)**8192).endswith("0"):
                cara=str((hash_carac.index(text[i])+8192)**8192)[::str((hash_carac.index(text[i])+8192)**8192).index("0")]
            else:
                cara=str((hash_carac.index(text[i])+8192)**8192)
                newtext=newtext+cara
        else:
            raise HashintError("'"+car+"' is not hashable")
    return newtext
