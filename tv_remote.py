import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["trt"],kanal = "trt" ):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_aç(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık")
        else:
            print("Televizyon Açılıyor")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı")
        else:
            print("Televizyon Kapatılıyor")
            self.tv_durum = "Kapalı"

    def ses_ayarları(self):
        while True:
            ses = input("Sesi Azalt: <\nSesi Artıır: > Çıkış: q\n")
            if ses == "<":
                if self.tv_ses > 0:
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)
                elif self.tv_ses == 0:
                    print("Ses:",self.tv_ses)
            elif ses == ">":
                if self.tv_ses < 10:
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)
                elif self.tv_ses == 10:
                    print("Ses:",self.tv_ses)
            elif ses.lower() == "q":
                print("Ses Güncellendi:",self.tv_ses)
                break
            else:
                print("Geçersiz İşlem")

    def kanal_ekle(self,kanal_ismi):
        zaten_mevcut_kanallar =[]
        eklenen_kanallar = []
        kanallar = kanal_ismi.split()
        for kanal in kanallar:
            if kanal not in self.kanal_listesi:
                self.kanal_listesi.append(kanal)
                eklenen_kanallar.append(kanal)
            else:
                zaten_mevcut_kanallar.append(kanal)
        if len(eklenen_kanallar) == 0:
            print("Hiç Kanal Eklenemedi")
            
        else:
            if len(eklenen_kanallar) == 1:
                print(f"{eklenen_kanallar[0]} Kanalı Eklendi")
            else:
                eklenen_kanallar_str = ",".join(eklenen_kanallar)
                print(f"{eklenen_kanallar_str} Kanalları Eklendi")
        if len(zaten_mevcut_kanallar) == 0:
            pass
        elif len(zaten_mevcut_kanallar) == 1:
                print(f"{zaten_mevcut_kanallar[0]} Kanalı Zaten Mevcut")
        else:
            zaten_mevcut_kanallar_str =",".join(zaten_mevcut_kanallar)
            print(f"{zaten_mevcut_kanallar_str} Kanalları Zaten Mevcut")            
        
    def kanal_sil(self,kanal_ismi):
        kanallar = kanal_ismi.split()
        silinen_kanallar = []
        bulunamayan_kanallar = []
        for kanal in kanallar:
            if kanal in self.kanal_listesi:
                self.kanal_listesi.remove(kanal)
                silinen_kanallar.append(kanal)
            else:
                bulunamayan_kanallar.append(kanal)
        if len(silinen_kanallar) == 0:
            print("Hiç Kanal Silinemedi")
        else:
            if len(silinen_kanallar) == 1:
                print(f"{silinen_kanallar[0]} Kanalı Silindi")
            else:
                silinen_kanallar_str = ",".join(silinen_kanallar)
                print(f"{silinen_kanallar_str} Kanalları Silindi")
        if len(bulunamayan_kanallar) == 0:
            pass
        elif len(bulunamayan_kanallar) == 1:
            print(f"{bulunamayan_kanallar[0]} Kanalı Bulunamadı")
        else:
            bulunamayan_kanallar_str = ",".join(bulunamayan_kanallar)
            print(f"{bulunamayan_kanallar_str} Kanalları Bulunamadı")



    def kanal_rasgele(self):
        if self.kanal_listesi:
            rasgele = random.randint(0, len(self.kanal_listesi))
            self.kanal = self.kanal_listesi[rasgele]
        else:
            print("Kanal Bulunamadı")
    def __str__(self):
        return "Tv Durumu: {}\nTv Ses: {}\nKanal Listesi: {}\n Aktif Kanal:{}".format(self.tv_durum,self.tv_ses, self.kanal_listesi, self.kanal)

kumanda = Kumanda()

print("""
*******************************
       TELEVİZYON İŞLEMLERİ
      
1- Televizyonu Aç
      
2- Televizyonu Kapat
      
3- Ses Ayarları
      
4- Kanal Ekle
      
5- Kanal Sil
      
6- Rasgele Kanal Aç
      
7-Televizyon Bilgileri

Çıkmak için 'q' ya basın
*******************************
""")

while True:
    işlem = input("Yapmak İstediğiniz İşlem:")
    if işlem == "q":
        print("Program Sonlandırılıyor")
        break
    elif işlem == "1":
        kumanda.tv_aç()
    elif işlem == "2":
        kumanda.tv_kapat()
    elif işlem == "3":
        kumanda.ses_ayarları()
    elif işlem == "4":
        while True:
            kanal_ismi = input("Eklenecek Kanalları Girin: Çıkış: q\n")
            if kanal_ismi.lower() == "q":
                break
            else:
                kumanda.kanal_ekle(kanal_ismi)

    elif işlem == "5":
        while True:
            kanal_ismi = input("Silinecek Kanalları Girin: Çıkış: q\n")
            if kanal_ismi.lower() == "q":
                break
            else:
                kumanda.kanal_sil(kanal_ismi)
    elif işlem == "6":
        kumanda.kanal_rasgele()
        print(f"{kumanda.kanal} Kanalı Açıldı")
    elif işlem == "7":
        print(kumanda)
    else:
        print("Geçersiz İşlem")