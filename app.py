print("## PROGRAM PYTHON MENGHITUNG LUAS SEGITIGA")
print("==========================================")
print()

def HitungLuasSegitiga(a,t):
        return round(0.5 * a * t,2)

 alas = float(input("Input Alas Segitiga"))
 tinggi = float(input("Input Tinggi segitiga"))

 print('Luas Segitiga =', HitungLuasSegitiga(alas,tinggi))
 print()