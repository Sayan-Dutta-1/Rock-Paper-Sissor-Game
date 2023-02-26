
import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='r':
        if you=='p':
            return True
        elif you=='s':
            return False
    elif comp=='p':
        if you=='s':
            return True
        elif you=='r':
            return False
    elif comp=='s':
        if you=='r':
            return True
        elif you=='p':
            return False

print("computer's turn: chose between rock(r) paper(p) sissor(s)")
xy= random.randint(1,3)
if xy==1:
    comp = 'r'
elif xy==2:
    comp = 'p'
elif xy==3:
    comp = 's'
you = input("your turn: chose between rock(r) paper(p) sissor(s) - ")
a=game(comp,you)

print(f"computer chose {comp}")
print(f"you chose {you}")

if a==None:
    print("its a tie")
elif a==True:
    print("you won")
else:
    print("computer won")
