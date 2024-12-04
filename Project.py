def hitung_IMT(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan / 100) ** 2

def hitung_berat_badan_ideal(tinggi_badan, kelamin):
    if kelamin.lower() == "pria":
        return (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.10)
    elif kelamin.lower() == "wanita":
        return (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)
    else:
        return None

def hitung_BMR(berat_badan, tinggi_badan, usia, kelamin):
    if kelamin.lower() == "pria":
        return 66 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
    elif kelamin.lower() == "wanita":
        return 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
    else:
        return None

# Input dari pengguna
berat_badan = float(input("Berat badanmu (kg): "))
tinggi_badan = float(input("Tinggi badanmu (cm): "))
usia = int(input("Usiamu (tahun): "))
kelamin = input("Kelaminmu (pria/wanita): ")

# Perhitungan
imt = hitung_IMT(berat_badan, tinggi_badan)
berat_badan_ideal = hitung_berat_badan_ideal(tinggi_badan, kelamin)
bmr = hitung_BMR(berat_badan, tinggi_badan, usia, kelamin)

# Output
print("\nHasil Perhitungan:")
print(f"IMT: {imt:.2f}")
print(f"Status Berat Badan: ", end="")
if imt < 18.5:
    print("Kekurangan berat badan")
elif 18.5 <= imt <= 24.9:
    print("Normal (ideal)")
elif 25.0 <= imt <= 29.9:
    print("Kelebihan berat badan")
else:
    print("Kegemukan (obesitas)")

print(f"Berat Badan Ideal: {berat_badan_ideal:.2f} kg")
print(f"BMR (Basal Metabolic Rate): {bmr:.2f} kalori/hari")
