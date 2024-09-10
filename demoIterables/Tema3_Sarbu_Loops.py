"""
Task1: Create a list of countries and check if "Japan" is in the list. Print a message based on the result.
Task2: Create a list of numbers from 1 to 10, then create a new list containing only the even numbers using list comprehension. Print the new list.
Task3: Write a Python program that calculates the sum of all even numbers between 1 and 100 using a for loop.
Example: Output 2550.

Task4: Write a loop to print all key-value pairs in the dictionary.
Task5: Check if the key email exists in the dictionary. If it doesn't exist, add it with a default value None.

Task6: Write a program that prints the numbers from 1 to 50. For multiples of 3, print "Fizz" instead of the number, for multiples of 5 print "Buzz," and for numbers that are multiples of both 3 and 5, print "FizzBuzz."

Task7: Write a Python program that calculates the sum of all even numbers between 1 and 100.

Task8: Ask the user to enter a word and write a Python program that checks if the word is a palindrome (a word that reads the same forward and backward).

Advanced:
Task9: Task: Create a nested dictionary representing a student database. Each key is a student ID, and the value is another dictionary containing name, age, and courses (a list of course names). Access and print the courses for a specific student.

Task10: Write a function that identifies all the duplicate elements in a list.
"""
#####from main_iterables import my_list###?


def find_in_list_of_countries (country_list,country):
    print(f"Task1: Create a list of countries and check if Japan is in the list. Print a message based on the result.")
    index = 0
    print (f"My list of countries is: {country_list}")
    for country in country_list:
        if country_list[index] == country:
            index= index + 1
    if index== len(country_list):
        print(f"Country {country} is in the list")
    else:
        print(f"Country {country} is NOT in the list")
    print("---------------")

def int_list(len):
    print("Task2: Create a list of numbers from 1 to 10, then create a new list containing only the even numbers using list comprehension. Print the new list.")
    generated_list = list(range (0, len))
    print(f"my generated list is: {generated_list}")
    #lenght= len(generated_list)
    my_new_list = generated_list[0::2]
    #print(f"My new list is: {generated_list[0::2]}")
    print(f"My new list is: {my_new_list}")
    print("---------------")

def sum_of_even_numbers_in_list(len):
    print(f"Task3: Write a Python program that calculates the sum of all even numbers between 1 and 100 using a for loop.")
    generated_list = list(range(0, len))
    even_generated_list = generated_list[1::2]
    print(f"My even generated numbers in the list are: {even_generated_list}")
    sum=0
    for index in generated_list:
        sum= sum + generated_list[index]
    print(f"The sum of even numbers in the list is: {sum}")
    print("---------------")

def my_persons_dictionary ():
    person_dictionary = {
        "name": ["Robert", "Anamaria"],
        "city": ["Cluj", "Malchen"],
        "age": [47, 30],
        "occupation": ["Inginer", "Tester"]
    }
    return person_dictionary

def print_my_dictionary():
    print("# Task4: Write a loop to print all key-value pairs in the dictionary.")
    dictionary= my_persons_dictionary()
    #for index in dictionary
    print(dictionary)
    #for i in dictionary["name"][0])
    #print (dictionary["name"][0])
    #print (len(dictionary))
    print(dictionary.keys())
    print(dictionary.items())
    print(dictionary.values())
    print("----------")
    for key, value in dictionary.items():
        #for string_values in values:
        #print(f"{key}:{value}")
        print(f"{key}: {dictionary[key][0]}")
    print("----------")
    for key, value in dictionary.items():
        #for string_values in values:
        #print(f"{key}:{value}")
        print(f"{key}: {dictionary[key][1]}")
    print("----------")

def search_in_my_dictionary():
    print("#Task5: Check if the key email exists in the dictionary. If it doesn't exist, add it with a default value None.")
    dictionary= my_persons_dictionary()
    i=1
    for key in dictionary.keys():
        if key != "email":
            i=0
    print(dictionary)
    if i==0:
        dictionary.update({"email" : ["None","None"]})
    print(dictionary)
    print("----------")

def gen_list_and_replace_values(len,Fizz,Buzz, FizzBuzz):
    print("# Task6: Write a program that prints the numbers from 1 to 50.")
    print("# For multiples of 3, print Fizz instead of the number,")
    print("# for multiples of 5 print Buzz, and for numbers that are multiples of both 3 and 5, print FizzBuzz")
    #list_range = range (1, len+1)
    generated_list= list (range(1, len+1))
    #print(generated_list)
    for index in generated_list:
        if index % 3 == 0 and index % 5 == 0:
            generated_list[index - 1] = FizzBuzz
            index= index + 1
        elif index % 3 == 0:
             generated_list[index-1]=Fizz
        elif index % 5 == 0:
            generated_list[index - 1] = Buzz
    print(generated_list)

def sum_of_even_values(num):
    print("#Task7: Write a Python program that calculates the sum of all even numbers between 1 and 100.")
    generated_list = list (range(1, num+1))
    print(generated_list)
    sum=0
    for i in generated_list:
        if i % 2 == 0:
            sum = sum + i
    print(f"The sum of even number is: {sum}")

def check_if_palindrome():
    # Task8: Ask the user to enter a word and write a Python program that checks if the word is a palindrome
    # (a word that reads the same forward and backward).
    print("Type a word: ")
    user_input = input()
    counter=-1
    for int in user_input:
        if int == user_input[counter]:
            counter = counter +1
    if counter == 1:
        print (f"{user_input} is a palindrome")
    else:
        print(f"{user_input} is NOT a palindrome")

def print_student_from_database():
    # Task9: Task: Create a nested dictionary representing a student database.
    # Each key is a student ID, and the value is another dictionary containing name, age, and courses (a list of course names).
    # Access and print the courses for a specific student.
    student_1= {
        "name": "Sarbu",
        "age": 31,
        "courses": ["python", "math"]
    }
    student_2 = {
        "name": "Milan",
        "age": 22,
        "courses": ["english", "python", "math"]
    }
    # prints the database
    print("My student database is:")
    student_database = {
        "student_1": student_1,
        "student_2": student_2
    }

    print(student_database)
    #What student you want to search
    print("Type the name of the student you want to be found:")
    user_input= input()
    index=0
    for x, object in student_database.items():
        #print("----")
        #print(f"{x}:")
        for y in object:
            if object[y] == user_input:
                print(f"Student is found: {object}")
                index=1
    if index != 1:
        print("Student is NOR found")

def create_database():
    print("----database-----")
    continue_loop = "y"
    index=0
    while continue_loop != "n":
        print("enter the Students' name:")
        name= input ()
        while name == "":
            print("enter the Students' name:")
            name = input()
        print("enter the Students' age:")
        age= input ()
        print("enter the Students' courses:")
        courses = input()
        student_key = "student" + str(index)
        student_key = {
            "name": name,
            "age": int(age),
            "courses": [courses]
            }
        if index == 0:
            database = {
                "student_key": student_key
            }
        index= index+1
        database.update(student_key,)
        print (database)
        print("Do you want to continue? y/n:")
        continue_loop=input()
    print(database)
"""
my_list = range (0, 10)
my_list_new= list (range(0, 10))
print(my_list)
print(type(my_list))
print("----")
print (my_list_new)
print(type(my_list_new))
"""

if __name__ == "__main__":

    """"
    #Task1: Create a list of countries and check if Japan is in the list. Print a message based on the result.
    country_list = ["Italy", "Romania", "Germany", "Bulgaria", "Japan"]
    find_in_list_of_countries(country_list,"Japan")
    #Task2: Create a list of numbers from 1 to 10, then create a new list containing only the even numbers using list comprehension. Print the new list.
    int_list(10)
    #Task3: Write a Python program that calculates the sum of all even numbers between 1 and 100 using a for loop.
    sum_of_even_numbers_in_list(100)
    #Task4: Write a loop to print all key-value pairs in the dictionary.
    print_my_dictionary()
"""
    #Task5: Check if the key email exists in the dictionary. If it doesn't exist, add it with a default value None.
    # search_in_my_dictionary()

    #Task6: Write a program that prints the numbers from 1 to 50.
    #For multiples of 3, print "Fizz" instead of the number,
    #for multiples of 5 print "Buzz," and for numbers that are multiples of both 3 and 5, print "FizzBuzz."
    # gen_list_and_replace_values(50,"Fizz","Buzz", "FizzBuzz")

    #Task7: Write a Python program that calculates the sum of all even numbers between 1 and 100.
    #sum_of_even_values(100)

    # Task8: Ask the user to enter a word and write a Python program that checks if the word is a palindrome
    # (a word that reads the same forward and backward).
    # check_if_palindrome()

   #Task9: Task: Create a nested dictionary representing a student database.
    # Each key is a student ID, and the value is another dictionary containing name, age, and courses (a list of course names).
    # Access and print the courses for a specific student.
    # print_student_from_database()
    create_database()
