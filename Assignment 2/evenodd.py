var1= raw_input("enter a number: ")
if int(var1) % 2 ==0:
    print "The number is even"
else:
    print ' the number is odd'
if int(var1) % 4 ==0:
    print " the number is a multiple of 4"
else:
    print " the number is not divisible by 4"

num = int(raw_input("enter number a "))
check = int(raw_input("enter number b "))
c = int(num)/ int(check)

if type(c) == int:
    print " a is divisible by b"
else:
    print " a is not divisible by b"
