def factorial_using_recursion(n):
    if n==0:
        return 1
    else:
        return n * factorial_using_recursion(n-1)

number = int(input('enter the number: '))

result = factorial_using_recursion(number)

print("factorial of "+ str(number)+ " = " + str(result))
