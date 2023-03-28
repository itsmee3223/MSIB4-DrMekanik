# soal nomor 1 buat fungsi factorial
# looping
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

# recursion
def factorial_recursion(n):
    if (n==1 or n==0):
        return 1
     
    else:
        return (n * factorial_recursion(n - 1))


# soal nomor 2 buat fungsi factor
def factor(num):
   print("Faktor dari",num," adalah:")
   for i in range(1, num + 1):
       if num % i == 0:
           print(i)

num = 5
print("Nilai factorial dari ", num, factorial_recursion(num))
factor(num)