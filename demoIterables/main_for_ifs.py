def simple_if_function():
    my_variable = 13

    if my_variable >= 10:
        # action A
        print("my_variable is equal to 10")
    elif my_variable == 11:
        # action B.1
        print("my_variable is equal to 11")
    elif my_variable == 12:
        # action B.2
        print("my_variable is equal to 12")
    elif my_variable == 13:
        # action B.3
        print("my_variable is equal to 13")
    else:
        # action C
        print("my_variable is not equal to 10")


def simple_list_of_int_search(el_to_search_for):
    list_of_int_to_search_in = [1, 2, 3, 4, 5]
    if el_to_search_for in list_of_int_to_search_in:
        print("Element was found")
    else:
        print("Element was not found")


def simple_list_search(el_to_search_for):
    list_of_elements = [1, 2, 3, 4, 5, "MyString", "Late", True]
    # Here I am searching for an element in the list
    if el_to_search_for in list_of_elements:
        print("Element was found")
    else:
        print("Element was not found")


def print_elements_from_list_using_for(my_list):
    """
    Description: This function will iterate through a list.
    :param my_list:
    :return: None
    """
    # Task1: If 5 is in the list, do nothing
    # Task2: If 6 is reached only once, continue with the code,
    # but if 6 is reached a second time, stop.
    counter = 0
    for var in my_list:
        if var == 5:
            break
        elif var == 6:
            counter = counter + 1
            if counter == 1:
                print(var)
            else:
                break
        else:
            print(type(var))
            print(var)


# Task3: Let the user decide how many loops to print
def print_with_while(user_limit):
    counter = 0
    while counter < user_limit:
        print(f"Printing ... {counter}")
        counter = counter + 1

if __name__ == "__main__":
    # mylist = [1, 2, 6, 3, "MyString", 5, 4, 6, 6, 7, 8, 9, 10]
    # mylist = [1, 2, 6, 6, 7]
    # print_elements_from_list_using_for(mylist)
    print("How many loops do you want to print?")
    # Waits for the user to input his thoughts and desires
    user_input = input()
    print(type(user_input))
    # Transforms (casts) the string to a integer
    user_input = int(user_input)
    print(type(user_input))
    # call the print_with_while() function passing the user_input as parameter
    print_with_while(user_input)
    