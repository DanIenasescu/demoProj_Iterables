def print_my_dictionary(dict_key, value_for_list):
    # This will print out my dictionary
    # Updated: Task 3: Add a new element to the dictionary element that has a list for a value
    my_dictionary = {
        "key1": "value1",
        "key2": 123,
        "mumu": True,
        "list": ["green", "yellow", "red", "pink", "white"]
    }
    print(my_dictionary)
    #Get list from dictionary
    value = my_dictionary[dict_key]
    print(value)
    # Modify the list
    value.append(value_for_list)
    print(value)
    # Update the dictionary
    my_dictionary.update({dict_key: value})
    print(f"Acesta este dicitonarul meu {my_dictionary}")


if __name__ == '__main__':
    dictionary_key = "list"
    value_to_be_added = 45
    print_my_dictionary(dictionary_key, value_to_be_added)
