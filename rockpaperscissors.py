

a = ['rock', 'paper', 'scissors']
b = ['rock', 'paper', 'scissors']

x = raw_input("user 1: rock, paper, scissors?")
y = raw_input("user 2: rock, paper scissors?")
if x == y :
    print "its a tie"
elif x == "rock" and y == "paper":
    print "y is winner"
elif x == "rock" and y == "scissors":
    print "y is winner"
elif x == "paper" and y == "rock":
    print "x is winner"
elif x == "paper" and y == "scissors":
    print "y is winner"
elif x == "scissors" and y == "rock":
    print "y is winner"
elif x == "scissors" and y == "paper":
    print "x is winner"
