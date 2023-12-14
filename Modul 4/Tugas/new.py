import math

def translasi(p, tx, ty):
    x, y = p
    return x + tx, y + ty

def dilatasi(p, sx, sy):
        x, y = p
        return x * sx, y * sy

def rotasi(p, sudut):
    x, y = p
    new_x = x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut))
    new_y = x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
    return new_x, new_y

def transformasi_decorator(function):
    def function(p, tx, ty, sudut, sx, sy):
        p_t = translasi(p, tx, ty)
        p_r = rotasi(p_t, sudut)
        p_s = dilatasi(p_r, sx, sy)
        return p_s
    return function

def user_input():
     tx = float(input("tx : "))
     ty = float(input("ty : "))
     sudut = float(input("sudut : "))
     sx = float(input("sx : "))
     sy = float(input("sy : "))
     return tx, ty, sudut, sx, sy

def line_equation_of(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    m = (y2 - y1) / (x2 - x1)

    c = y1 - m * x1

    return f"y = {m:.2f}x + {c:.2f}"

@transformasi_decorator
def transformasi(p, tx, ty, sudut, sx, sy):
    return p, tx, ty, sudut, sx, sy


#Titik Awal
titik_A = (2,7)
titik_B = (7,0)


user_data = user_input()

new_titik_A = transformasi(titik_A, *user_data)
new_titik_B = transformasi(titik_B, *user_data)

print("Persamaan garis yang melalui titik " + str(titik_A) + " dan " + str(titik_B)+ " :")
print(line_equation_of(titik_A, titik_B))

print("Persamaan garis baru setelah transformasi:")
print(line_equation_of(new_titik_A, new_titik_B))