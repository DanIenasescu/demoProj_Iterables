myVar = 10

def my_function():
    global myVar
    myVar = 20
    return myVar

if __name__ == "__main__":
    print("Hello")
    print("myVar: {0}".format(myVar))
    my_function()
    print("myVar: {0} and a string: {1}".format(myVar, "string_var"))