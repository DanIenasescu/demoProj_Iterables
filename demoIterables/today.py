def key_value_pairs():
    # Task 4
    print('-----------------------------')
    my_dictionary = {
        'name': 'Elena',
        'age': 28,
        'hobby': 'snowboarding'
    }
    # print(my_dictionary)

    for key, value in my_dictionary.items(): #items -> method
        # print(key, ':', value)
        print(f"{key}:{value}")


    # Task 5
    print('-----------------------------')
    if 'email' not in my_dictionary.keys():
        my_dictionary['email'] = None

    for key, value in my_dictionary.items():
        # if 'email' not in my_dictionary.keys():
        #     my_dictionary['email'] = None
        #     break
        # print("debug2")
        print(key, ':', value)
    print(my_dictionary)

def some_func(param1: str) -> str:
    """
    Description: This is just a demo func.
    :param param1: str - Description: I pass the torch
    :return: str, Charcoals
    """
    print(param1)
    return "something"

def my_colleague_wrote_this_function(param1="defaultValue"):
    print(param1)
    return "toSender"

def another_function(param1, param2="MyVar", param3=1):
    print(param1)
    print(param2)
    print(param3)
    return True

def yet_another_function(*args):
    """
    Description: Please pass 4 values
    :param args:
    :return:
    """
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])

def last_annoying_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")

if __name__ == "__main__":
    # another_function(param1=1, param3=2)
    # yet_another_function(1, 2, 3, 4, 5, 6)
    last_annoying_function(key1="arg", five="this")
