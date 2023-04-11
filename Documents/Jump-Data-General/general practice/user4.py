from collection2 import add_employee
import yaml

# add employees to the yaml file
testuser = add_employee()
testuser2 = add_employee()
testuser3 = add_employee()

# write the new employees to the yaml file
with open("user.yaml", 'w') as file:
    data = yaml.dump([testuser, testuser2, testuser3])
    file.write(data)
