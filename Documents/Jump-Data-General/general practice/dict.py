# declare the keys and values in a dict literal of the inputs
dict = {
    "name": input("What is your name:"),
    "age": input("What is your age:"),
    "years coding": input("How many years have you been coding:")
}

# create input variables

first = input("What is your first programming languages")
second = input("What is your second programming languages")
third = input("What is your third programming languages")

#create a tuple literal

first_three_languages = (
    first,
    second,
    third
)

# favorite input variables

first_favorite = input("What is your first favorite programming languages")
second_favorite = input("What is your second favorite programming languages")
third_favorite = input("What is your third favorite programming languages")

# create a list literal with our new variables

favorite_three_languages = [first_favorite, second_favorite, third_favorite]

# use intersect to add a second argument to set

set = set(first_three_languages).intersection(favorite_three_languages)

dict["first_three_languages"] = first_three_languages
dict["set"] = set
dict["favorite three languages"] = [first_favorite, second_favorite, third_favorite]

print(dict)
