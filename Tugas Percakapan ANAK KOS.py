#PERCAKAPAN TEMAN KOST
# 1. Class & Objek Dasar
class Kost:
    pass

class Penghuni:
    pass

kost1 = Kost()
kost2 = Kost()

print(type(kost1))
print(type(kost2))

penghuni1 = Penghuni()
penghuni2 = Penghuni()

print(type(penghuni1))
print(type(penghuni2))


# 2. Instance Attribute
penghuni1 = Penghuni()
penghuni1.kamar = 8
penghuni1.nama = "Omeh"

print(penghuni1.kamar)
print(penghuni1.nama)

penghuni2 = Penghuni()
penghuni2.kamar = 7
penghuni2.nama = "Intan"

print(penghuni2.kamar)
print(penghuni2.nama)


# 3. Class Attribute 
class Kost:
    nama_kost = "Kost Andini Putri"  
    alamat = "Kp.Lebak Gempol"

kost = Kost()
print(kost.nama_kost)
print(kost.alamat)

class Penghunibaru:  
    kamar = 7
    nama = "Intan"

penghuni_baru = Penghunibaru()
print(penghuni_baru.kamar)
print(penghuni_baru.nama)


# 4. Class, Objek, & Method (Percakapan)
class Penghuni:
    kamar = 0
    nama = ""
    alamat = ""
    kampus = ""
    jurusan = ""

    def perkenalan(self):
        print(f"{self.nama}: Halo salam kenal, nama aku {self.nama} penghuni lama disini")

    def hello(self, nama_lawan):
        print(f"{self.nama}: Halo {nama_lawan}, salam kenal juga aku {self.nama}, aku baru pindah kesini")

    def tanya_kamar(self, nama_lawan):
        print(f"{self.nama}: Oh {nama_lawan}, kamu di kamar berapa?")

    def jawab_kamar(self):
        print(f"{self.nama}: Aku kamar {self.kamar}")

    def tanya_alamat(self):
        print(f"{self.nama}: Alamat kamu darimana?")

    def tanya_kuliah(self):
        print(f"{self.nama}: Kamu kuliah dimana?")

    def respon_kuliah_sama(self):
        print(f"{self.nama}: Oh kita sama, aku juga kuliah disana! Kamu jurusan apa?")

    def jawab_jurusan(self):
        print(f"{self.nama}: Aku jurusan {self.jurusan}")

    def penutup(self):
        print(f"{self.nama}: Okedeh senang berkenalan sama kamu, kalo ketemu sapa aku ya!")


# Membuat Objek
omeh = Penghuni()
omeh.nama = "Omeh"
omeh.kamar = 8
omeh.alamat = "Sawarna"
omeh.kampus = "Uniba"
omeh.jurusan = "Sistem Informasi"

intan = Penghuni()
intan.nama = "Intan"
intan.kamar = 7
intan.alamat = "Bayah"
intan.kampus = "Uniba"
intan.jurusan = "Pendidikan Jasmani"

# Jalannya Percakapan
omeh.perkenalan()
intan.hello(omeh.nama)

omeh.tanya_kamar(intan.nama)
print(f"Intan: Aku kamar {intan.kamar}")

# Intan bertanya balik soal kamar dan Omeh menjawab
print(f"Intan: Kalo kamu kamar berapa {omeh.nama}?")
omeh.jawab_kamar()

omeh.tanya_alamat()
print(f"Intan: Aku dari {intan.alamat}")

omeh.tanya_kuliah()
print(f"Intan: Aku kuliah di {intan.kampus}")

omeh.respon_kuliah_sama()
print(f"Intan: Aku jurusan {intan.jurusan}")

# Intan balik bertanya jurusan dan Omeh menjawab
print(f"Intan: Kalo kamu jurusan apa {omeh.nama}?")
omeh.jawab_jurusan()

omeh.penutup()
