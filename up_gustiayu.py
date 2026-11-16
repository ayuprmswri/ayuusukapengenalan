# input
jumlah = int(input("Jumlah mahasiswa: "))
data = []
lulus = 0
tidak_lulus = 0

# proses
for i in range(1, jumlah + 1):
    nama = input(f"\nNama mahasiswa {i}: ")
    nilai = int(input("Nilai: "))

    if nilai >= 85:
        grade, ket = "A", "Sangat Baik"
        status = "Lulus"
        lulus += 1
    elif nilai >= 75:
        grade, ket = "B", "Baik"
        status = "Lulus"
        lulus += 1
    elif nilai >= 60:
        grade, ket = "C", "Cukup"
        status = "Lulus"
        lulus += 1
    else:
        grade, ket = "D", "Tidak Lulus"
        status = "Tidak Lulus"
        tidak_lulus += 1

    data.append((nama, nilai, grade, ket, status))

print("\n===== HASIL PENILAIAN =====")
for nama, nilai, grade, ket, status in data:
    print(f"{nama} | Nilai: {nilai} | {grade} ({ket}) | {status}")

print(f"\nJumlah lulus       : {lulus}")
print(f"Jumlah tidak lulus : {tidak_lulus}")