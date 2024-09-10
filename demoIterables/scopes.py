# global section
global_var = 1234

def funct():
    # local section
    global global_var
    my_local_var = global_var + 1234
    my_local_var = my_local_var + 14
    global_var = 123
    print(f"global_var printed inside the function has the value {my_local_var}")

def funct2(para1):
    global global_var
    if global_var == 123:
        print("Operation failed! global_var is already 123.")
    else:
        print("global_var changed")
        global_var = para1

if __name__ == "__main__":
    print(f"First print: {global_var}")
    funct()
    print(f"Second print: {global_var}")
