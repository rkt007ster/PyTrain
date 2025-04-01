
# Task 2: Sum of Integers from 1 to 50 Using a Loop

def __main__():
    j = 0
    for i in range(1,51):
        j = i + j

    print(f"The sum of numbers from 1 to 50 is: {j}" )

__main__()