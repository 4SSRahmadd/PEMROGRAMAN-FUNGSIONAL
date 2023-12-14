import matplotlib.pyplot as plt
from functools import reduce

nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]
mahasiswa = list(map(lambda i: f'{i+1}', range(len(nilai_mahasiswa))))

def avg_nilai(nilai_mahasiswa):
    total_nilai = reduce(lambda x, y: x + y, nilai_mahasiswa)
    average = total_nilai / len(nilai_mahasiswa)
    return average

rata_rata = avg_nilai(nilai_mahasiswa)

print('Mahasiswa\t\t\t:', mahasiswa)
print('Nilai mahasiswa\t\t\t:', nilai_mahasiswa)
print('Rata-rata nilai mahasiswa\t: {:.2f}'.format(rata_rata))

plt.figure(figsize=(10, 5))
plt.axhline(y=rata_rata, color='red', linestyle='dashed', linewidth=2, label=f'Rata-rata = {rata_rata:.2f}')
plt.plot(rata_rata)
plt.bar(mahasiswa, nilai_mahasiswa)
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.legend()
plt.show()