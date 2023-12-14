def point(x, y):
    return x, y

def line_equation_of(p1, M):
    def calculate_c(point):
        x1, y1 = point
        return y1 - M * x1

    C = calculate_c(p1)
    return f"y = {M:.2f}x + {C:.2f}"

# Ganti input sesuai dengan 3 digit NIM terakhir
print("Persamaan garis yang melalui titik (2,7) dan bergradien 0:")
print(line_equation_of(point(2, 7), 0)) 