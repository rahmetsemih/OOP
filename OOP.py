
# !  DONT MODIFY THIS CLASS
class Insan():
    def __init__(self, isim, yas, sehir):
        self.isim = isim
        self.yas = yas
        self.sehir = sehir
        self.hobi = []

    def hobi_ekle(self, hobi):
        self.hobi.append(hobi)

    def bilgi(self):
        if self.hobi == []:
            ...
        else:
            print("Hobileri:")
            for i, j in enumerate(self.hobi):
                print(i+1, "-", j)
        print(f"{self.isim} {self.yas} yaşındadır ve {self.sehir}'lidir.")


class Ogrenci(Insan):
    ogrenciler = []

    def __init__(self, isim, yas, sehir, egitim_seviyesi):
        super().__init__(isim, yas, sehir)
        self.egitim_seviyesi = egitim_seviyesi

        self.ogrenciler.append(self.isim)

    def bilgi(self):
        super().bilgi()
        print(f"{self.isim} {self.egitim_seviyesi} eğitim seviyesinde öğrencidie.")

    @staticmethod
    def ort_hesap(a, b):
        print(f"yıl sonu ortalaması: {(a+b)/2}")

    @classmethod
    def liste_goster(cls):
        if cls.ogrenciler == []:
            print("Öğrenci listesi boş.")
        else:
            for i, j in enumerate(cls.ogrenciler):
                print(i+1, "-", j)


def test():
    print("-"*50)
    insan = Insan("Semih", 20, "İstanbul")
    insan.hobi_ekle("spor")
    insan.hobi_ekle("yemek")
    insan.bilgi()

    print("-"*50)
    ogrenci = Ogrenci("Semih", 20, "İstanbul", "Universite")
    ogrenci.hobi_ekle("spor")
    ogrenci.hobi_ekle("yemek")
    ogrenci.bilgi()

    print("-"*50)
    ogrenci2 = Ogrenci("Ali", 10, "İstanbul", "Orta")
    ogrenci2.hobi_ekle("spor")
    ogrenci2.hobi_ekle("yemek")
    ogrenci2.bilgi()

    print("-"*50)
    Ogrenci.liste_goster()
    Ogrenci.ort_hesap(10, 20)

if __name__ == "__main__":
    test()
