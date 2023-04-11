from user_funct import user_input

# name

# first split the input into two indexes
name = input("What is your full name?: ").split(" ")
# assign variables to each index
first_name, last_name = name[0], name[1]
# capitalize those variables
new_first_name, new_last_name = first_name.capitalize(), last_name.capitalize()

# age

# you can wrap the input in a built in int function
age = int(input("What is your age?: "))
# subtract from the current year
birth_year = 2023 - age

# email

email = first_name + "." + last_name + birth_year[2:] + "@comapny.com"

# print everything
printed = False

# ask for our number
num = int(input("Pick a number between 1 and 100: "))

while printed == False:

    try:
        user_input(num)
        print(new_first_name, new_last_name, age, birth_year, email)
        printed = True
    except:
        "Please pick a valid number between 1 and 100"
