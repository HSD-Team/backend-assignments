import json

print("---Uye Kayit Defteri---")
while True:
    user_choose = int(input("1)Ekle  2)Listele  3)Ara  4)Sil  5)Cikis\nYapmak istediginiz islemi secin: " ))
    match user_choose:
        case 1:
            print("---Kullanici Ekleme Islemi---")
            isim = input("Isminizi giriniz: ")
            rol = input("Rolunuzu giriniz (ornek: yazilimci): ")
            diller = input("Bildiginiz dilleri virgul (,) ile ayirark giriniz: ").split(",")
            with open("members.json", "w", encoding="utf-8") as dosya:
                json.dump({"isim": isim,"rol": rol,"diller": diller}, dosya, ensure_ascii=False, indent=4)
            #dosyanin kayit oldugu yeri coz ve sadece tek veri kaydediyor 
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            print("Cikis isleminiz gerceklestiriliyor...")
            break
        case _:
            print("Gecersiz bir numara girdiniz. Lutfen tekrar deneyiniz.")
        


        
        
