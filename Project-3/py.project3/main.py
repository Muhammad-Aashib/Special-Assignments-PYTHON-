import random

def play():
    user = input("What's Your Choice? 'r' for rock, 'p' for paper, and 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "tie"
    
    if iswin(user, computer):
        return "you Won!"
    
    return "you Lost!"
    
def iswin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print(play())