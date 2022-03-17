# Recursion / Rekursif function

# function yang memanggil functionya sendiri, hingga mengeluarkan output
def showNumber(n) :
    # blok if bisa disebut base case, kondisi akhir dari rekursif yang menghasilkan nilai
    if (n == 0) :
        return 
    # base case digunakan untuk menghentikan rekursif, agar tidak infinite loop
    print(n)
    return showNumber(n-1)
# showNumber(10)

def factorial(n) :
    if(n == 0) : 
        return 1
    return n * factorial(n-1)

print(factorial(5))
""" 
    factorial(5)
    5 * factorial(4)
    5 * (4 * factorial(3))
    5 * (4 * (3 * factorial(2)))
    5 * (4 * (3 * (2 * factorial(1)))
    
    5 * (4 * (3 * (2 * 1 )))
    5 * (4 * (3 * 2))
    5 * (4 * 6)
    5 * (24)
    120
"""

""" 
    Kegunaan Rekursif
    - menggantikan looping
    - fibonanci
    - dll
"""