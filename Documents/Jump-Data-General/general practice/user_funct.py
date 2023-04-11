#define the method at the top of the page
def user_input(num):
    if num <= 100 and num >= 1:
        print(f"The number is within the range: {num}")
        return True
    else:
        raise Exception
