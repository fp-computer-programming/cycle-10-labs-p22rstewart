# Author RTS 2/2/22

# Define the function
def divisible(x):
    # Create open list
    result = []
    # Create for loop
    for y in x:
        if y > 500:
            break
        # Check to see if its divisible by 5
        elif y % 5 == 0 & y <= 150:
            result.append(y)
        return result


# Test
print(divisible([0]))
print(divisible([10]))
print(divisible([27]))
print(divisible([193]))