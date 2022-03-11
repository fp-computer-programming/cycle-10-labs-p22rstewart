# Author RTS 2/2/22

# Defining the function
def sum_all(number): 
    # Variables 
    result = 0 
    x = 0 
    # While loop
    while x < number: 
        result += x + 1
        x += 1
    return result

# Tests
print(sum_all(2))
print(sum_all(10))
print(sum_all(15))
