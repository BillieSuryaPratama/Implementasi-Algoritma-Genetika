import pandas as pd

# Membaca data makanan
karbohidrat = pd.read_csv('MakananKarbohidrat.csv')
protein = pd.read_csv('MakananProtein.csv')
lemak = pd.read_csv('MakananLemak.csv')
serat = pd.read_csv('MakananSerat.csv')


# Menambahkan kategori makanan
karbohidrat['Kategori'] = 'Karbohidrat'
protein['Kategori'] = 'Protein'
lemak['Kategori'] = 'Lemak'
serat['Kategori'] = 'Serat'

# Menggabungkan semua data
data_makanan = pd.concat([karbohidrat, protein, lemak, serat], ignore_index=True)

# 1. Input dari pengguna
berat_badan = float(input("Berat badanmu (kg): "))
tinggi_badan = float(input("Tinggi badanmu (cm): "))
usia = int(input("Usiamu (tahun): "))
kelamin = input("Kelaminmu (pria/wanita): ")

# Pilihan tingkat aktivitas
print("\nTentukan tingkat aktivitasmu:")
print("1. Sedentary (Jarang berolahraga)")
print("2. Lightly Active (Olahraga ringan 1-3 hari/minggu)")
print("3. Moderately Active (Olahraga sedang 3-5 hari/minggu)")
print("4. Very Active (Olahraga berat 6-7 hari/minggu)")
print("5. Extra Active (Olahraga sangat berat)")
tingkat_aktivitas = (input("Pilih tingkat aktivitas: "))

# 2. Hitung IMT
def hitung_IMT(berat_badan, tinggi_badan):
    return berat_badan / (tinggi_badan / 100) ** 2

# 3. Menentukan berat badan ideal
def hitung_berat_badan_ideal(tinggi_badan, kelamin):
    if kelamin.lower() == "pria":
        return (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.10)
    elif kelamin.lower() == "wanita":
        return (tinggi_badan - 100) - ((tinggi_badan - 100) * 0.15)
    else:
        return None

# 4. Menghitung kebutuhan kalori harian
def hitung_BMR(berat_badan, tinggi_badan, usia, kelamin):
    if kelamin.lower() == "pria":
        return 66 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia)
    elif kelamin.lower() == "wanita":
        return 655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia)
    else:
        return None
    
# 5. Menghitung Total Daily Energy Expenditure (TDEE)
def hitung_tdee(bmr, tingkat_aktifitas):
    if tingkat_aktifitas == "1" :
        return bmr * 1.2
    elif tingkat_aktifitas == "2" :
        return bmr * 1.375
    elif tingkat_aktifitas == "3" :
        return bmr * 1.55
    elif tingkat_aktifitas == "4" :
        return bmr * 1.725
    elif tingkat_aktifitas == "5" :
        return bmr * 1.9
    else:
        return None
    
# 6. Menentukan kebutuhan kalori
def hitung_kebutuhan_kalori(tdee, berat_badan, berat_badan_ideal):
    if berat_badan < berat_badan_ideal:
        return tdee + 500
    elif berat_badan > berat_badan_ideal:
        return tdee - 500
    return tdee

# Perhitungan
imt = hitung_IMT(berat_badan, tinggi_badan)
berat_badan_ideal = hitung_berat_badan_ideal(tinggi_badan, kelamin)
bmr = hitung_BMR(berat_badan, tinggi_badan, usia, kelamin)
tdee = hitung_tdee(bmr, tingkat_aktivitas)
kebutuhan_kalori = hitung_kebutuhan_kalori(tdee, berat_badan, berat_badan_ideal)

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
print(f"TDEE (Total Daily Energy Expenditure): {tdee:.2f} kalori/hari")
print(f"Kebutuhan kalori harianmu untuk mencapai berat badan ideal: {kebutuhan_kalori:.2f} kalori/hari")