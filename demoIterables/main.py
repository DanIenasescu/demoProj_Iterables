def print_hi(name):
    print(f'Hi, {name}')
    print('Hi, Dan')
    # thislist will be used to showcase an example
    thislist = [
        "apple", 123, True, "apple", "cherry"
    ]
    print(thislist[0])
    print(thislist[1])
    print(thislist[2])

# Task1: Create a list of numbers from 1 to 5 and print the second and last elements in the list.
def task1_print_first_and_last_list_item(list_of_items):
    print("--------------")
    print(list_of_items[1])
    print(list_of_items[-1])

# This is the main section of the program
if __name__ == '__main__':
    # print_hi('Dan')
    my_list = [1, 2, 3, 4, 5]
    task1_print_first_and_last_list_item(my_list)
    # ---------------------------------------------
    my_list = [5, 6, 7, 8, 9, 6]
    task1_print_first_and_last_list_item(my_list)
    # ---------------------------------------------
    my_list = [5, 6, 7]
    task1_print_first_and_last_list_item(my_list)
