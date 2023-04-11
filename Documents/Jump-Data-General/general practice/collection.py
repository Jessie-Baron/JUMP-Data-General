collection = {

}

def comprehend(collection):

    for dict in collection:
        new_el = dict['employee_status'] = 'new'
        dict.update(new_el)
        print(dict)

def add_employee():
    employee = {
        "first_name": input("What is your first name: ").capitalize(),
        "last_name": input("What is your last name: ").capitalize(),
        "age": input("What is your age: "),
        "email": input("What si your email: ")
    }

    dict = employee
    collection.update(dict)
    print(collection)
