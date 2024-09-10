# del function
def simple_del_function():
    # declare and initialize a variable
    my_var = 10
    print(my_var)
    # deletes the variable completely, meaning
    # you will lose the variable after calling the def statement
    del my_var
    # after deleting the variable, if you want to use the variable
    # as an argument, you cannot, because it was deleted
    # That's why the next line will throw an error :)
    print(my_var)

def simple_del_list_el_function():
    # declare and initialize a list variable
    list_of_el = [1, 2, 3, 4, 5, 6]
    print(list_of_el)
    # you can use the "del" statement to erase an item from a list
    # without deleting the whole list
    del list_of_el[2]
    print(list_of_el)
    # careful! you can easily delete the list variable,
    # by call delete on the whole list
    del list_of_el
    # after deleting the variable, if you want to use the variable
    # as an argument, you cannot, because it was deleted
    # That's why the next line will throw an error :)
    print(list_of_el)

simple_del_list_el_function()