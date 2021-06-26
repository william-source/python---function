# class
class Mahasiswa():
    __universitas = "UKP"
    jumlah_mahasiswa = 0
    __nilai = 0
    jumlah_osis = 0
    
    def __init__(self,input_nama,input_umur,input_jurusan):
        self.nama = input_nama
        self.umur = input_umur
        self.jurusan = input_jurusan
        
        Mahasiswa.jumlah_mahasiswa += 1
    
    def ujian(self, input_nilai):
        self.__nilai = input_nilai
        
    def showAll(self):
        
        if(self.jumlah_mahasiswa>=2):
            print("===========================")
        else:
            print("==== DAFTAR MAHASISWA ====")
    
        print("Nama :", self.nama)
        print("Umur :", self.umur)
        print("Jurusan :", self.jurusan)
        print("Universitas :", self.__universitas)
        if(self.__nilai != 0):
            print("nilai :", self.__nilai)
        else:
            print("Mahasiswa belum ujian !")

class Osis(Mahasiswa):
        
    # def __init__(self):
    #     Mahasiswa.jumlah_osis +=1
    
    def bagian(self, input_organisasi,input_jabatan,input_masa):
        self.organisasi = input_organisasi
        self.jabatan = input_jabatan
        self.masa = input_masa
        Mahasiswa.jumlah_osis+=1
    
    def showOsis(self):
        print("\n")
        print("Organisasi :",self.organisasi)
        print("Jabatan :",self.jabatan)
        print("Masa Jabatan :",self.masa,"tahun")

# main code
william = Mahasiswa("william sean wiyogo", 21, "Informatika")
william.ujian(100)
william.showAll()

abraham = Mahasiswa("Abraham Imanuel", 20, "ekonomi")
abraham.showAll()

zenza = Osis("Zenza Bronica", 20, "hukum")
zenza.bagian("hima", "ketua", 2)
zenza.ujian(100)
zenza.showAll()
zenza.showOsis()

andre = Osis("Andreas ", 20, "tata boga")
andre.bagian("humas", "bawahan", 100)
andre.showAll()
andre.showOsis()




print("\n")
print("Jumlah Mahasiswa :",Mahasiswa.jumlah_mahasiswa)
print("\n")
print("Jumlah Osis : ",Mahasiswa.jumlah_osis)


