# Lambda Function

# small anonymous function
# lambda dapat menerima beberapa argument, tetapi hanya 1 expression

# lamda arguments : expression
x = lambda n : n * 2
print(x(4))

# 2 argument
x = lambda a , b : a / b
print(x(6, 2))

# 3 argument
x = lambda a,b,c : a + b + c
print(x(2,4,6))

# lambda biasanya digunakan didalam function / pengganti inner function yang hanya memiliki 1 expression
def myfunc(n) : 
    """ def kali(a) : 
        return a * n """   
    return lambda a : a * n

kali = myfunc(4)
print(kali(5))