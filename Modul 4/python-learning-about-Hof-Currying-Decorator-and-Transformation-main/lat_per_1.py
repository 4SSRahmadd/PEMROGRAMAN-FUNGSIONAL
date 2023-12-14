def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Hof fungsi dalam fungsi
kali_dua = perkalian(20)
result = kali_dua(21)
print(result)

# currying percabangan variable 
kali_dua = perkalian(2)
hasil = kali_dua(70)
print(hasil)
