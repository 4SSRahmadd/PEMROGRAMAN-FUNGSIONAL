Data = [
    "3 minggu 3 hari 7 jam 21 menit",
    "5 minggu 5 hari 8 jam 11 menit",
    "7 minggu 1 hari 5 jam 33 menit",
]

filtered_data = []

for data in Data:
    data_split = data.split()
    temp = filter(lambda x: x.isdigit(), data_split)
    filtered_data.append(list(temp))

for data in filtered_data:
    print(data)