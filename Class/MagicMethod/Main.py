# magic method ~ method bawaan python, yang ditandai dengan double underscore __

class Car :
    # init ~ digunakan sebagai konfigurasi untuk object yang di-construct
    def __init__(self, brand, type) :
        self.brand = brand
        self.type = type

    # str ~ dipanggil ketika sebuah instan dari kelas yang bersangkutan dikonversi menjadi string atau ketika dijadikan parameter untuk fungsi print().
    def __str__(self) :
        return f"{self.type} adalah mobil dari brand {self.brand}"

    # repr ~ sama seperti str, tetapi biasanya digunakan ketika Debugging
    def __repr__(self) :
        return f"Debug : {self.type} adalah mobil dari brand {self.brand}"
    
    @property
    def __dict__(self) :
        return "Objeck ini memiliki brand dan type"

supra = Car("Toyota", "Supra Mk-4")
print(supra.type)
print(supra)
# penggunaan untuk repr
print(repr(supra))
print(supra.__dict__)