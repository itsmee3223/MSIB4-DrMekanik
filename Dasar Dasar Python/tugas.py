def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

print(factorial(5))

def factor(num):
   print("Factor",num,"adalah:")
   for i in range(1, num + 1):
       if num % i == 0:
           print(i)

factor(100)