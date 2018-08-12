# Python if else statements
# 1) Check if the number is even or odd
def even_or_odd(number):
    if number==0:
        print("Number is zero")
    elif number%2 == 0:
        print("%s is even" %number)
    else:
        print("%s is odd" %number)

# 2) Hackerrank if-else problem solution 
#   https://www.hackerrank.com/challenges/py-if-else/problem
# we will make them functions for easier testing:
def py_if_else(number):
    if (number%2 != 0) or (number%2==0 and  6<= number <= 20):
        print("Weird")
    else:
        print("Not Weird")



if __name__ == '__main__':
    even_or_odd(45)
    py_if_else(3)

