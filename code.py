import random
compscore = 0
userscore = 0
q = int(input("How many rounds you want to play?"))
print("Wish you good luck.")
i=1
for i in  range(q):

    a = str(input("S for stone, P for paper and K for scissor."))
    lst = ("S", "P", "K")
    if a == "S":
        b = random.choice(lst)
        print("Computer choosed",b)
        if a == b:
            print("Draw")
        elif b == "P":
            print("Computer got one point.")
            compscore = compscore + 1
        elif b == "K":
            print("User score one point.")
            userscore = userscore + 1
        print("your score is", userscore)
        print("computer's score is", compscore)
    if a == "P":
        c = random.choice(lst)
        print("Computer choosed",c)
        if a == c:
            print("Draw")
        elif c == "S":
            userscore+=1
            print("User got one point.")
        elif c == "K":
            compscore+=1
            print("Computer got one point")
        print("Your score is", userscore)
        print("Computer's score is",compscore)
    if a == "K":
        d = random.choice(lst)
        print("Computer choosed",d)
        if a == d:
            print("Draw")
        elif d == "S":
            compscore+=1
            print("Computer got one point.")
        elif d == "P":
            userscore+=1
            print("User got one point.")
        print("Your score is",userscore)
        print("Computer's score is", compscore)

print("Your final score is", userscore)
print("Computer's final score is", compscore)
if userscore > compscore:
    print("You Win")
elif compscore > userscore:
    print("Computer wins")
elif compscore == userscore:
    print("Match Draw")
    
print("Thank you for playing.")
