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

def task1_print_first_and_last_list_item(list_of_items):
# Task1: Create a list of numbers from 1 to 5 and print the second and last elements in the list.
    print("--------------")
    print(list_of_items[1])
    print(list_of_items[-1])

def task2_change_colors(color):
# Task2: Change the second element in a list of colors to "blue" and print the updated list.
    print("--------------")
    list_of_colors = ["green", "yellow", "red", "pink", "white"]
    list_of_colors[1] = color
    print(list_of_colors)


# This is the main section of the program
if __name__ == '__main__':
    # # print_hi('Dan')
    # my_list = [1, 2, 3, 4, 5]
    # task1_print_first_and_last_list_item(my_list)
    # # ---------------------------------------------
    # my_list = [5, 6, 7, 8, 9, 6]
    # task1_print_first_and_last_list_item(my_list)
    # # ---------------------------------------------
    # my_list = [5, 6, 7]
    # task1_print_first_and_last_list_item(my_list)
    task2_change_colors("blue")
