# Argument dan Parameter

def salam(nama): # yang terdapat disebelah nama function disebut parameter
    print(f"Halo {nama}")

salam("Paul") # ini disebut argument lalu dikirimkan ke parameter

# 2 argument
def salam(nama, waktu): 
    print(f"Halo {nama}, Selamat {waktu}!")

salam("Rudi", "Malam")
# salam("Paul") # ERROR!, karena hanya memberikan 1 argumen padahal yang dibutuhkan 2

# arbitrary argument ~ memberikan argument yang tidak diketahui jumlahnya
def myFunc(*anak) : # memberikan * sebelum nama parameter
    print(f"anak bapak rudi adalah : {anak[2]} ")

myFunc("Sena","Willy","Niko")

# keyword argument
def myfunction(anak3, anak1, anak2) : 
    print(f"anak ke 3 bernama = {anak3}")

myfunction(anak1 = "Sena", anak2 = "Willy", anak3 = "Niko")

# Arbitrary keyword argument ~ memberikan argument yang tidak diketahui jumlahnya, tetapi menggunakan keyword
def namaLengkap(**anak) : 
    print(f'dia memiliki nama belakang = {anak["belakang"]}')

namaLengkap(depan = "Paul", belakang = "Mahardika")

# default parameter value
def asal(kota = "Jakarta") :
    print(f"Saya berasal dari kota {kota}")

asal("Solo")
asal() # akan menggunakan nilai default, jika tidak mengirimkan argument

# list sebagai argument 
print("\nList For Argument")
def my_func(food) :
    for x in food: 
        print(x)

fruits = ["apple","banana","watermelon"]

my_func(fruits)
