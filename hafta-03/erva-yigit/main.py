import json

print("---Uye Kayit Defteri---")
while True:
    try:
        user_choose = int(input("1)Ekle  2)Listele  3)Ara  4)Sil  5)Cikis\nYapmak istediginiz islemi secin: " ))
    except ValueError:
        user_choose = -1
    match user_choose:
        case 1:
            print("---Kullanici Ekleme Islemi---")
            isim = input("Isminizi giriniz: ").strip()
            rol = input("Rolunuzu giriniz (ornek: yazilimci): ").strip()
            if isim == "" or rol == "":
                print("Isim ve rol bos birakilamaz.")
                continue
            diller = input("Bildiginiz dilleri virgul (,) ile ayirark giriniz: ").split(",")
            yeni_uye = {"isim": isim, "rol": rol, "diller": diller}
            try:
                with open("hafta-03/erva-yigit/members.json", "r", encoding="utf-8") as uyeler_dosyasi:
                    uyeler_listesi = json.load(uyeler_dosyasi)
            except (FileNotFoundError, json.JSONDecodeError):
                uyeler_listesi = []
            uyeler_listesi.append(yeni_uye)
            with open("hafta-03/erva-yigit/members.json", "w", encoding="utf-8") as uyeler_dosyasi:
                    json.dump(uyeler_listesi, uyeler_dosyasi, ensure_ascii=False, indent=4)
            print("Kullanici basariyla eklendi.")
        case 2:
            print("---Kayitli Üyeler---")
            try:
                with open("hafta-03/erva-yigit/members.json", "r", encoding="utf-8") as uyeler_dosyasi:
                    uyeler_listesi = json.load(uyeler_dosyasi)
                if len(uyeler_listesi) == 0:
                    print("Sistemde henüz kayitli üye bulunmuyor.")
                else:
                    sayac = 1
                    for uye in uyeler_listesi:
                        print(f"{sayac}) İsim: {uye['isim']} | Rol: {uye['rol']} | Diller: {uye['diller']}")
                        sayac += 1
            except (FileNotFoundError, json.JSONDecodeError):
                print("Sistemde henüz kayitli üye bulunmuyor (Dosya yok).")
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Cikis isleminiz gerceklestiriliyor...")
            break
        case _:
            print("Gecersiz bir numara girdiniz. Lutfen tekrar deneyiniz.")
        


        
        
