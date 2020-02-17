voted={}

def check_voter():
    name = input("Please input your name for voting!")
    if voted.get(name):
        print ("kick them out")
        check_voter()
    else:
        voted[name]= True
        print ("Let them voted!")
        check_voter()


check_voter()