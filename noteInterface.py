import noteCore as core
from getpass import getpass

uid = 0

def sep():
    print("---------------")

def loginScreen():
    global uid
    print("1.Sign In\n2.Sign Up")
    choice = int(input("Choose : "))
    if choice == 1:
        uname = input("Username : ")
        passwd = getpass()
        uid = core.userLogin(uname,passwd)
        if uid == False:
            print("Username or Password incorrect")
        else:
            print("Welcome")
    elif choice == 2:
        uname = input("Username : ")
        passwd = getpass()
        core.userRegistration(uname,passwd)
    sep()

def mainMenu():
    print("MoteApp")
    print("1.List All")
    print("2.Add")
    print("3.Remove")
    #print("4.Change")
    print("0.Exit")
    choice = int(input("Choose : "))
    sep()

    if choice == 1:
        noteNumbers = core.noteGetNumbers(uid)
        for num in noteNumbers:
            print(core.noteGet(uid,num))
    elif choice == 2:
        title = input("Title : ")
        txt = input("Note : ")
        core.noteAdd(uid,title,txt)
    elif choice == 3:
        noteNumbers = core.noteGetNumbers(uid)
        for num in noteNumbers:
            print(core.noteGet(uid,num))
        sep()
        noteNumber = input("Note Number : ")
        sep()
        print(core.noteRemove(uid, noteNumber))
    sep()
    

while uid == False:
    loginScreen()
while uid != False:
    mainMenu()