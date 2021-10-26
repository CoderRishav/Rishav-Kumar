import json
global data
global loginstate
loginstate=0
data=json.load(open("example_2.json"))
cred={}
def login():
    print("Enter Login Credentials")
    print("Enter user name : ")
    un=input()
    print("Enter Password : ")
    p=input()
    if un not in cred:
        print("enter Valid user name")
        return
    if cred[un]==p:
        print("Login successful.")
        global loginstate
        loginstate=1
    else:
        print("Enter correct password.")
        return

def register():
    print("Set Username: ")
    un=input()
    print("Set Password : ")
    p=input()
    cred[un]=p
    print("Registration Successful")
    print("--------------------------------------")
    login()

def main_page():
    print("=========WELCOME TO QUIZ APP==========")
    print("--------------------------------------")
    print("SELLECT LOGIN MODE")
    print("1 - SUPER USER")
    print("2 - USERS")
    print("3 - EXIT")
    im=int(input())
    if im==1:
        if loginstate:
            super_user()
        else:
            print("--------------------------------------")
            print("1 - login")
            print("2 - Register")
            print("--------------------------------------")
            ip=int(input())
            if ip==1:
                login()
                main_page()
            elif ip==2:
                register()
                main_page()

    elif im==2:
        if loginstate:
            user()
        else:
            print("--------------------------------------")
            print("1 - login")
            print("2 - Register")
            print("--------------------------------------")
            ip=int(input())
            if ip==1:
                login()
                main_page()
            elif ip==2:
                register()
                main_page()

    else:
        exit()
        
def vq():
    for i in data:
        print("--------------------------------------")
        print("Topic - ",i)
        print("--------------------------------------")
        for j in data[i]:
            print("Difficulty Level:",j['dif'])
            print("Question : ",j['question'])
            print("Options : ")
            for k in j['options']:
                print(k) 
        print("--------------------------------------")
    print("redirecting to prev menu.")
    super_user()
    
def vt():
    print("--------------------------------------")
    print("Topics : ")
    for i in data:
        print(i)
    print("--------------------------------------")
    print("redirecting to prev menu.")
    super_user()

def et():
    print("Enter the topic you want to modify : ")
    old=input()
    print("Enter the new value for the topic : ")
    new=input()
    data[new]=data[old]
    del data[old]
    print("redirecting to prev menu.")
    super_user()

def dt():
    print("Enter the topic you want to delete : ")
    val=input()
    del data[val]
    print("redirecting to prev menu.")
    super_user()

def ct():
    print("Enter the new Topic : ")
    nt=input()
    data[nt]=[]
    super_user()

def dq():
    print("Enter the Topic to delete : ")
    nt=input()
    data[nt]=[]
    super_user()

def cq():
    print("enter topic")
    t=input()
    qd={}
    print("Select the difficulty level :")
    print("Easy")
    print("Medium")
    print("Hard")
    dif = input()
    qd['dif'] = dif
    print("Enter the question : ")
    qn=input()
    qd['question']=qn
    print("Enter the options : ")
    op=[]
    for i in range(4):
        op.append(input())
    qd['options']=op
    print("enter the correct answer : ")
    ans=input()
    qd['answer']=ans
    data[t].append(qd)
    super_user()

def super_user():
    print("1 - View Quizzes")
    print("2 - Create Quiz")
    print("3 - Edit Quiz")
    print("4 - Delete Quiz")
    print("5 - Create Topic")
    print("6 - View Topics")
    print("7 - Edit Topics")
    print("8 - Delete Topics")
    print("9 - Logout")
    ip=int(input())
    if ip==1:
        vq()
    elif ip==2:
        cq()
    elif ip==3:
        cq()
    elif ip==4:
        dq()
    elif ip==5:
        ct()
    elif ip==6:
        vt()
    elif ip==7:
        et()
    elif ip==8:
        dt()
    elif ip==9:
        print("redirecting to main menu from there you can exit.")
        main_page()
        global loginstate
        loginstate=0
    else:
        print("Enter valid input")
        super_user()
    

def take_quiz():
    print("HI..!!!! Please enter Your name")
    name= input()
    print("--------------------------------------")
    for i in data:
        print(i)
    print("--------------------------------------")
    print("Select a topic from the above list : ")
    topic=input()
    tq=len(data[topic])
    tm=0
    print("--------------------------------------")
    for j in data[topic]:
        print(j['question'])
        print("options : ")
        for k in j['options']:
            print(k)
        print("Enter answer : ")
        ans=input()
        if ans==j['answer']:
            print("--------------------------------------")
            print("Correct")
            tm+=1
        else:
            print("--------------------------------------")
            print("Incorrect")
        print("--------------------------------------")
    print(name,":Thanks for giving test")
    print("and you have scored",tm,"marks out of",tq)
    print("and Correct answers are:")
    for j in data[topic]:
        print(j['answer'])
    user()

def user():
    print("1 - Take Quiz")
    print("2 - Logout")
    ip=int(input())
    if ip==1:
        take_quiz()
    else:
        global loginstate
        loginstate=0
        main_page()
main_page()

