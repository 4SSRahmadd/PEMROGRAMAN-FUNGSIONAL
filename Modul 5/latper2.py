import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 3, 4, 5, 6])
ypoints = np.array([3, 5, 5, 7, 1, 4])

plt.figure(figsize=(10, 5))
plt.title('Grafik Penjualan Liquid 2020')
plt.plot(xpoints, ypoints, color='red', marker='o')
plt.xlim([0, 8])
plt.ylim([0, 8])
plt.xticks(xpoints, labels=["Jan", "Feb", "Mar", "Apr",
           "Mei", "Jun"])
plt.xlabel('Bulan', fontsize=15)
plt.ylabel('Pengeluaran', fontsize=15)
plt.show()
