#define the method at the top of the page
def user_input(num):
    if num <= 100 and num >= 1:
        print(f"The number is within the range: {num}")
    else:
        raise TypeError("The number is outside the range")

# ask for our number
num = int(input("Pick a number between 1 and 100: "))

# as long as we have a number we will call the method and either print the number or raise an error
while num:
    user_input(num)
    break
