# TODO 0 : Import library lain yang dibutuhkan
from PIL import Image, ImageDraw, ImageFont

# TODO 1: Lakukan load image pada variabel berikut
# hint: kalian bisa gunakan fungsi open()
gambarku = Image.open("assets/kartel.jpg")

# TODO 2: Ubah gambar menjadi hitam-putih
# hint: kalian bisa gunakan fungsi convert()
gambarBW = gambarku.convert("L")

# TODO 3: Tambahkan text sesuai kriteria.
draw = ImageDraw.Draw(gambarBW)
font = ImageFont.truetype("arial.ttf", 100)
text = "Yaasir Rahmat Kautsar - 202110370311270"
bbox = draw.textbbox((0, 0), text, font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
text_x = (gambarku.width - text_width) // 2
text_y = (gambarku.height - text_height) // 2
draw.text((text_x, text_y), text, font=font, fill="white")

# TODO 4: Simpan gambar hasil edit menggunakan fungsi save()
gambarBW.save("assets/percobaan1.png")

# TODO 5: Tampilkan hasil akhir gambar
gambarBW.show()