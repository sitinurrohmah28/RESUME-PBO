class Mahasiswa:
    nim = 0
    nama = ""

    def perkenalan(self):
        print(f"Halo nama saya {self.nama}")

    def hello(self, nama):
        print(f"Hallo {self.nama}, nama saya {nama}")


mahasiswa = Mahasiswa()
mahasiswa.nama = "Omeh"
mahasiswa.perkenalan()
mahasiswa.hello("Intan")
