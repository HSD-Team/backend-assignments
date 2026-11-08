import json

def normalize(metin):
    metin = metin.replace("İ", "i").replace("I", "i").replace("ı", "i")
    return metin.lower()
class MemberNotFoundError(Exception):
    pass

print("\n---Uye Kayit Defteri---")
while True:
    try:
        user_choose = int(input("\n1)Ekle  2)Listele  3)Ara  4)Sil  5)Cikis\nYapmak istediginiz islemi secin: " ))
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
                        uye_dil = ", ".join(uye["diller"])
                        if uye_dil == "":
                            uye_dil ="-"
                        print(f"{sayac}) İsim: {uye["isim"]} | Rol: {uye["rol"]} | Diller: {uye_dil}")
                        sayac += 1
            except (FileNotFoundError, json.JSONDecodeError):
                print("Sistemde henüz kayitli üye bulunmuyor (Dosya yok).")

        case 3:
            print("---Kullanici Arama Islemi---")
            aranan_isim = input("Aramak istediginiz kisinin ismini giriniz: ").strip()
            if aranan_isim == "":
                print("Lutfen gecerli bir isim giriniz.")
                continue
            try:
                with open("hafta-03/erva-yigit/members.json", "r", encoding="utf-8") as uyeler_dosyasi:
                    uyeler_listesi = json.load(uyeler_dosyasi)
                bulundu = False
                for uye in uyeler_listesi:
                    if normalize(uye["isim"]) == normalize(aranan_isim):
                        uye_dil = ", ".join(uye["diller"])
                        if uye_dil == "":
                            uye_dil = "-"
                        print(f"-> İsim: {uye['isim']} | Rol: {uye['rol']} | Diller: {uye_dil}")
                        bulundu = True
                        break
                if bulundu == False:
                    print(f"'{aranan_isim}' isminde bir kayit bulunamadi.")
            except FileNotFoundError:
                print("Sistemde kayitli üye bulunmuyor.")

        case 4:
            print("---Kullanici Silme Islemi---")
            silinecek_isim = input("Silmek istediginiz kisinin ismini giriniz: ").strip()
            try:
                with open("hafta-03/erva-yigit/members.json", "r", encoding="utf-8") as uyeler_dosyasi:
                    uyeler_listesi = json.load(uyeler_dosyasi)
                silindi = False
                for uye in uyeler_listesi:
                    if normalize(uye["isim"]) == normalize(silinecek_isim):
                        uyeler_listesi.remove(uye)
                        silindi = True
                        break
                if not silindi:
                    raise MemberNotFoundError(
                        f"MemberNotFoundError\n'{silinecek_isim}' isminde bir uye bulunamadi."
                    )
                with open("hafta-03/erva-yigit/members.json", "w", encoding="utf-8") as uyeler_dosyasi:
                    json.dump(uyeler_listesi, uyeler_dosyasi, ensure_ascii=False, indent=4)
                print(f"{uye['isim']} adli kullanici sistemden basariyla silindi.")
            except MemberNotFoundError as hata:
                print(hata)
            except FileNotFoundError:
                print("Sistemde kayitli üye bulunmuyor.")

        case 5:
            print("Cikis isleminiz gerceklestiriliyor...")
            break

        case _:
            print("Gecersiz bir numara girdiniz. Lutfen tekrar deneyiniz.")
        