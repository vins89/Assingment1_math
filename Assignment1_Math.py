#from click._compat import raw_input


def math(vars):

    var1 = raw_input("what is your first value? ") #rawinput converted to string
    var2 = raw_input("enter second value ")

    print(int(var1) + int(var2))

    print (int(var1) * int(var2))

    var1 = raw_input("enter third value ")
    var2 = raw_input("enter fourth value ")

    print(int(var1) + int(var2))

    var2 = int(raw_input("enter what ever value "))
    print (var2)


math(vars)
