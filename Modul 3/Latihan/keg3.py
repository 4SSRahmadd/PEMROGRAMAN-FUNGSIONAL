random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Filter untuk memisahkan nilai float, int, dan string
float_values = list(filter(lambda x: isinstance(x, float), random_list))
int_values = list(filter(lambda x: isinstance(x, int), random_list))
string_values = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
new_int_values = []
for number in int_values:
    satuan = number % 10
    puluhan = (number // 10) % 10
    ratusan = number // 100
    new_int_values.append({"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan})

# Output
print("Data Float:", float_values)
print("Data Int:")
for item in new_int_values:
    print(item)
print("Data String:", string_values)