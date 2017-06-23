def math():
    var1 = raw_input("what is your name ")  # rawinput converted to string
    var2 = raw_input("What is your age? ")
    var3 = 80 - int(var2)
    if 80 <= var3:
        print " number of years it will take you to turn 80 is " ,var3
    else:
        print " you are already 80 year old"



math()
