# Task4: Create a list of 10 items and print it
# 0 - start index
# 10 - end index
# 3 - step
my_list = list(range(0, 10, 3))
# print(my_list)

#get the data
list_of_data_to_go_through = [
    123,    4,      5,      2,      234,    65,
    123,    624563, 1234,   734,    23,     451234,
    6,      7,      537,    2345,   23154,  6
]

# print(f"List is {len(list_of_data_to_go_through)} long")

# Task5: Print every 5th element from the list
#Process the data
for var in range(0, len(list_of_data_to_go_through), 5):
    print(f"List el: {list_of_data_to_go_through[var]} at index {var}")
