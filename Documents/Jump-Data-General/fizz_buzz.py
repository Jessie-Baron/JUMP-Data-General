
nums = input("Input a number: ")

list = []
sum = 0

for i in range(1, int(nums + 1)):
    if(i % 3 == 0 and i % 5 == 0):
        list.append("Fizzbuzz")
    elif(i % 3 == 0):
        list.append("Fizz")
    elif(i % 5 == 0):
        list.append("Buzz")
    else:
        list.append(i)
        sum += i + 1

print(
    "sum of integers:", sum
      , "count of Fizz:", list.count("Fizz")
      , "count of Buzz", list.count("Buzz")
      , "count of Fizzbuzz", list.count("Fizzbuzz")
      )
