voted={}
def check_voter(name):
    if voted.get(name):
        print ("kick them out")
    else:
        voted[name]= True
        print ("Let them voted!")

name = input("Please input your name!")
check_voter(name)