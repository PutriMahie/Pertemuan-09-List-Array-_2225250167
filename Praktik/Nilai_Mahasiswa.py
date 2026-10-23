def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


def nilai_lulus(data, batas=60):
    lulus = []

    for x in data:
        if x >= batas:
            lulus.append(x)

    return lulus


nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

rata = rata_rata(nilai)
lulus = nilai_lulus(nilai)

print(f"Nilai = {nilai}")
print(f"Rata-rata = {rata:.2f}")
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")