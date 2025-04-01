
#Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n < 2:
        return print(f"Factorial of {n} is: 1")
    else:
        val = 1
        for i in range(1, n+1):
            val = val * i
        return print(f"Factorial of {n} is: ", val)

factorial(5)