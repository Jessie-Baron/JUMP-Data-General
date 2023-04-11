import yaml
from nanoid import generate

# with yaml imported we can create employees and dump them into a yaml file
def add_employee():

    employee = {
        "id": generate(),
        "first_name": input("What is your first name: ").capitalize(),
        "last_name": input("What is your last name: ").capitalize(),
        "age": input("What is your age: "),
        "email": input("What si your email: ")
    }

    return employee
