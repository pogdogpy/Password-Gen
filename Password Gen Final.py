import random
import time
global auto
charlist=list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789!$%^&*()-_=+")
pissypass = "NULL"
auto = False
def check():
    global pissypass
    global stren
    global abort
    global auto
    stren = "null"
    abort = False
    if len(pas) < 8 or len(pas) > 24:
        if auto == False:
            print("Error. Password must be more than 8 characters long and less than 24!")
        abort = True
    score = len(pas)
    lowpoint = False
    cappoint = False
    numpoint = False
    sympoint = False  
    for char in pas:
        if char.islower():
            lowpoint = True
        if char.isupper():
            cappoint = True
        if char.isdigit:
            numpoint = True
        if char in charlist[62:73]:
            sympoint = True
        if char not in charlist:
            if auto == False:
                print("Error Password contains disallowed characters.")
            abort = True
   
    if lowpoint == True:
        score += 5
    else:
        score -= 5
    if cappoint == True:
        score += 5
    else:
        score -= 5
    if numpoint == True:
        score += 5
    else:
        score -= 5
    if sympoint == True:
        score += 5
    else:
        score -= 5
    
    if lowpoint == True and cappoint == True and numpoint == True and sympoint == True:
        score += 10
    
    pas.lower()
    paslist = []
    letterlist=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    for i in pas:
        if i in letterlist:
            paslist.append(i)
        else:
            paslist.append("_")
    for i in paslist:
        if i != "_":
            letind=letterlist.index(i)
            pasind=paslist.index(i)
            if (letind+1) == (pasind+1):
                if (letind+2) == (pasind+2):
                    score-=5            
   
    if score >= 20:
        stren = "strong"
    elif score <= 0:
        stren = "weak"
    else:
        stren = "medium strength"
    
    if abort == False:
        if auto == False:
            print("your password is "+stren)
            print("Your password's score was "+str(score)+"\n")
    if abort == False:
        pissypass = pas
while True:
    choice = input("Test Password Strength(1)\nGenerate Password(2)\nValidate(3)\nQuit(4)\n")
    if choice=="1":
        auto = False
        saved = False
        pas = input("Input Password\n")
        check()
    if choice == "2":
        auto = True
        saved = True
        length = random.randint(8,12)
        len2= int(length)
        stren = "null"
        while stren != "strong":
            allow = list("QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!$%^&*()-_=+")
            random.shuffle(allow)
            fpas = allow[0:len2]
            pas = ''.join(fpas)
            check()
        print(pas)
    if choice == "3":
        if saved == False:
            checkme = input("Input your password\n")
            if checkme == pissypass:
                print("Successfully validated.")
                saved == True
            else:
                print("Password invalid.")
        if saved == True:
            print("Your password is already successfully validated")
    if choice == "4":
        exit()
