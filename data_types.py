def main():
    while True:
        veri_tipi = input("Veri Tipini Giriniz(1: String 2: List 3: Set)\n")
        if veri_tipi == "1":
            string1 = input("Metin Girin:")
            string2 = input("Metin Girin:")
            metin_seçme(string1,string2)
        elif veri_tipi == "2":
            list1 = input("Liste Elemanlarını Girin:").split()
            list2 = input("Liste Elemanlarını Girin:").split()
            liste_seçme(list1,list2)
        elif veri_tipi == "3":
            set1 = input("Küme Elemanlarını Girin:").split()
            set2 = input("Küme Elemanlarını Girin:").split()
            küme_seçme(set1,set2)
        else:
            print("Geçersiz Veri Tipi Seçimi")
            continue

def metin_seçme(string1,string2):
    print("Metin1:", string1)
    print("Metin2:", string2)
    metin_seçim = input("Hangi Metin Açılsın, Çıkış: 'q'")
    if metin_seçim == "1":
        seçilen_metin = string1
        metin_işlem(seçilen_metin)
    elif metin_seçim == "2":
        seçilen_metin = string2
        metin_işlem(seçilen_metin)
    else:
        print("Geçersiz İşlem")

def liste_seçme(list1,list2):
    print("Liste1:", list1)
    print("Liste2:", list2)
    liste_seçim = input("Hangi Liste Açılsın, Çıkış: 'q'")
    if liste_seçim == "1":
        seçilen_liste = list1
        liste_işlem(seçilen_liste)
    elif liste_seçim == "2":
        seçilen_liste = list2
        liste_işlem(seçilen_liste)
    else:
        print("Geçersiz İşlem")

def küme_seçme(set1,set2):
    set1 = set(set1)
    set2 = set(set2)
    print("Küme1:", set1)
    print("Küme2:", set2)
    küme_seçim = input("Hangi Küme Açılsın, Çıkış: 'q'")
    if küme_seçim == "1":
        seçilen_küme = set1
        küme_işlem(seçilen_küme)
    elif küme_seçim == "2":
        seçilen_küme = set2
        küme_işlem(seçilen_küme)
    else:
        print("Geçersiz İşlem")

def metin_işlem(seçilen_metin):
    print("İşlem1: Küçük/Büyük Harf Yapma\nİşlem2: Harf Değiştirme\nİşlem3: Başlangıç/Bitiş Kontrol\nİşlem4: Seçilen Harfleri Ekle\nİşlem5: Seçilen Harfi Sil\nİşlem6: Seçilen Harf Kaç Defa Geçiyor\nİşlem7: Seçilen Harfi Ara\nİşlem0: Bilgileri Göster\nÇıkış: 'q'\n")
    while True:
        print("Seçilen Metin:", seçilen_metin)
        string_işlem = input("İşlem Seçin Çıkış: 'q'")
        if string_işlem == "1":
            büyük_küçük = input("Büyütmek İçin: '>'\nKüçültmek İçin: '<'\n")
            if büyük_küçük == ">":
                değişken = input("Büyüteceğiniz Harfi Girin:")
                if değişken in seçilen_metin:
                    seçilen_metin = seçilen_metin.replace(değişken, değişken.upper())
                    print("Metin Büyütüldü")
                else:
                    print("Seçilen Harf Bulunamadı")
            elif büyük_küçük == "<":
                değişken = input("Küçülteceğiniz Harfi Girin:")
                if değişken in seçilen_metin:
                    seçilen_metin = seçilen_metin.replace(değişken, değişken.lower())
                    print("Metin Küçültüldü")
                else:
                    print("Seçilen Harf Bulunamadı")
            elif büyük_küçük == "q":
                print("Çıkış Yapılıyor")
                break
            else:
                print("Geçersiz İşlem")
        elif string_işlem == "2":
            değişken = input("Değiştirilecek Harf: ")
            değiştir = input("Yerine Koymak İstediğiniz Harf: ")
            seçilen_metin = seçilen_metin.replace(değişken, değiştir)
            print("Harf Değiştirildi")
        elif string_işlem == "3":
            baş_bit = input("Başlangıcı Bulmak İçin: 'baş'\nBitişi Bulmak İçin: 'bit'\nÇıkış için 'q': ")
            değişken = input("Harf Seçin:")
            if baş_bit == "baş":
                if seçilen_metin.startswith(değişken):
                    print(f"Metin {değişken} ile başlıyor")
                else:
                    print(f"Metin {değişken} ile başlamıyor")
            elif baş_bit == "bit":
                if seçilen_metin.endswith(değişken):
                    print(f"Metin {değişken} ile bitiyor")
                else:
                    print(f"Metin {değişken} ile bitmiyor")
            elif baş_bit == "q":
                print("Çıkış Yapılıyor")
                break
            else:
                print("Geçersiz İşlem")
        elif string_işlem == "4":
            ekle = input("Eklenecek Harf: ")
            seçilen_metin += ekle
            print("Harf Eklendi")
        elif string_işlem == "5":
            sil = input("Silinecek Harf: ")
            seçilen_metin = seçilen_metin.replace(sil, "")
            print("Harf Silindi")
        elif string_işlem == "6":
            harf = input("Kaç defa geçtiğini öğrenmek istediğiniz harf: ")
            geçis_sayısı = seçilen_metin.count(harf)
            print(f"Seçilen harf {geçis_sayısı} kez geçiyor")
        elif string_işlem == "7":
            aranacak_harf = input("Aranacak Harf: ")
            if aranacak_harf in seçilen_metin:
                print("Harf bulundu")
            else:
                print("Harf bulunamadı")
        elif string_işlem == "0":
            print(f"Seçilen Metin: {seçilen_metin}")
        elif string_işlem == "q":
            print("Çıkış Yapılıyor")
            break
        else:
            print("Geçersiz İşlem")

def liste_işlem(seçilen_liste):
    print("İşlem1: Ekleme\nİşlem2: Temizleme\nİşlem3: Kopyalama\nİşlem4: Sayma\nİşlem5: Diğer Veriyi Ekle\nİşlem6: İndex Bulma\nİşlem7: Konuma Ekleme\nİşlem8: İndexteki Elemanı Silme\nİşlem9: Eleman Silme\nİşlem10: Ters Çevirme\nİşlem11: Sıralama\nİşlem0: Bilgileri Göster\nÇıkış: 'q'\n")
    while True:
        print("Seçilen Liste:", seçilen_liste)
        liste_işlem = input("Hangi İşlem Seçilsin: ")
        
        if liste_işlem == "1":
            eleman = input("Eklemek İstediğiniz Elemanı Girin:")
            eleman = eleman.split()
            if len(eleman) == 1:
                seçilen_liste.append(eleman[0])
                print("Eleman Eklendi")
            else:
                print("Lütfen Bir Adet Eleman Girin")
        elif liste_işlem == "2":
            seçilen_liste.clear()
            print("Liste Elemanları Temizlendi")
        elif liste_işlem == "3":
            kopyalanan_liste = seçilen_liste.copy()
            print(f"Liste Kopyalandı\nOrjinal Liste: {seçilen_liste}\nKopyalanan Liste: {kopyalanan_liste}")
        elif liste_işlem == "4":
            eleman = input("Kaç Kez Geçtiğini Öğrenmek İstediğiniz Elemanı Girin: ")
            geçis_sayısı = seçilen_liste.count(eleman)
            print(f"Seçilen eleman {geçis_sayısı} kere geçiyor")
        elif liste_işlem == "5":
            diğer_liste = list(input("Eklemek İstediğiniz Elemanlaı Girin: ").split())
            seçilen_liste.extend(diğer_liste)
            print("Seçilen Listenin Sonuna Diğer Liste Eklendi")
        elif liste_işlem == "6":
            eleman = input("İndexini bulmak istediğiniz eleman: ")
            if eleman in seçilen_liste:
                index = seçilen_liste.index(eleman)
                print(f"Elemanın İndexi: {index}")
            else:
                print("Eleman bulunamadı")
        elif liste_işlem == "7":
            index = int(input("Hangi İndexe Eklemek İstersiniz: "))
            eleman = input("Hangi Elemanı Eklemek İstersiniz: ")
            seçilen_liste.insert(index, eleman)
            print("Eleman Eklendi")
        elif liste_işlem == "8":
            index = int(input("Hangi İndexteki Elemanı Silmek İstersiniz: "))
            silinen_eleman = seçilen_liste.pop(index)
            print(f"Silinen Eleman: {silinen_eleman}")
        elif liste_işlem == "9":
            eleman = input("Silinecek Elemanı Girin: ")
            seçilen_liste.remove(eleman)
            print("Eleman Silindi")
        elif liste_işlem == "10":
            seçilen_liste.reverse()
            print("Liste Ters Çevrildi")
        elif liste_işlem == "11":
            seçilen_liste.sort()
            print("Liste Sıralandı")
        elif liste_işlem == "0":
            print(f"Seçilen Liste: {seçilen_liste}")
        elif liste_işlem == "q":
            print("Çıkış Yapılıyor")
            break
        else:
            print("Geçersiz İşlem")

def küme_işlem(seçilen_küme):
    print("İşlem1: Eleman Ekleme\nİşlem2: Küme Elemanları Ekleme\nİşlem3: Eleman Çıkarma\nİşlem4: Eleman Çıkarma\nİşlem5: Küme Elemanları Çıkarma\nİşlem6: Kesişim Elemanlarını Alma\nİşlem7: Birleşim Elemanlarını Alma\nİşlem8: Alt Küme Sorgulama\nİşlem9: Ayrık Küme Sorgulama\nİşlem10: Rasgele Eleman Çıkarma\nİşlem11: Kümeyi Temizle\nİşlem0: Küme Bilgilerini Sorgula\n")
    while True:
        işlem = input("Yapmak İstediğiniz İşlemi Girin:")
        if işlem == "1":
            değişken = input("Eklemek İstediğiniz Eleman:")
            if len(değişken) != 1:
                print("Birden Fazla Eleman Ekleyemezsin")
            elif len(değişken) == 1 and değişken not in seçilen_küme:
                seçilen_küme.add(değişken)
                print("Seçilen Eleman Eklendi")
            else:
                print("Eleman Zaten Mevcut")
        elif işlem == "2":
            değişken = set(input("Eklemek İstediğiniz Elemanları Girin:").split())
            seçilen_küme.update(değişken)
            print("Elemanlar Kümeye Eklendi")
        elif işlem == "3":
            değişken = input("Silmek İstediğiniz Eleman:")
            if len(değişken) != 1:
                print("Birden Fazla Eleman Çıkaramazsın")
            elif len(değişken) == 1 and değişken in seçilen_küme:
                seçilen_küme.remove(değişken)
                print("Seçilen Eleman Çıkarıldı")
            else:
                print("Eleman Bulunamadı")
        elif işlem == "4":
            değişken = input("Silmek İstediğiniz Elemanları Girin:").split()
            seçilen_küme.discard(değişken)
            print("Elemanlar Kümeden Silindi")            
        elif işlem == "5":
            değişken = set(input("Silmek İstediğiniz Elemanları Girin:").split())
            seçilen_küme.difference_update(değişken)
            print("Seçilen Elemanlar Silindi")
        elif işlem == "6":
            değişken = set(input("Kesişim Elemanlarını Almak İstediğiniz Kümeyi Girin:").split())
            seçilen_küme = seçilen_küme.intersection(değişken)
            print(f"Kümelerin Kesişim Elemanları Alındı")
        elif işlem == "7":
            değişken = set(input("Birleşim Elemanlarını Almak İstediğiniz Kümeyi Girin:").split())
            seçilen_küme = seçilen_küme.union(değişken)
            print(f"Kümelerin Birleşim Elemanları Alındı")
        elif işlem == "8":
            değişken = set(input("Alt Kümesi Olup Olmadığını Öğrenmek İstediğiniz Kümeyi Girin:").split())
            geçici_küme = seçilen_küme.copy()
            if değişken.issubset(seçilen_küme):
                print("Seçilen Küme Ana Kümenin Alt Kümesidir")
            else:
                print("Seçilen Küme Ana Kümenin Alt Kümesi Değildir")
        elif işlem == "9":
            değişken = set(input("Ayrık Küme Olup Olmadığını Öğrenmek İstediğiniz Kümeyi Girin:").split())
            geçici_küme = seçilen_küme.copy()
            if değişken.isdisjoint(seçilen_küme):
                print("Kümeler Ayrık Kümedir")
            else:
                print("Kümeler Ayrık Küme Değildir")
        elif işlem == "10":
            try:
                seçilen_küme = seçilen_küme.pop()
            except KeyError:
                print("Seçilen Küme Boş")
            print("Kümeden Rasgele Bir Eleman Çıkarıldı")
        elif işlem == "11":
            seçilen_küme = seçilen_küme.clear()
            print("Seçilen Küme Temizlendi")
        elif işlem == "0":
            print(f"Ana Küme:{seçilen_küme}\n")
        elif işlem == "q":
            print("Çıkış Yapılıyor")
            break
        else:
            print("Geçersiz İşlem")
            

main()
