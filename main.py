id_to_en = {"satu": "one", "dua": "two", "tiga": "three", "empat": "four", "lima": "five", "enam": "six", "tujuh": "seven", "delapan": "eight", "sembilan": "nine", "sepuluh": "ten"}
id_to_su = {"satu": "hiji", "dua": "dua", "tiga": "tilu", "empat": "opat", "lima": "lima", "enam": "genep", "tujuh": "tujuh", "delapan": "dalapan", "sembilan": "salapan", "sepuluh": "sapuluh"}
id_to_ja = {"satu": "siji", "dua": "loro", "tiga": "telu", "empat": "papat", "lima": "limo", "enam": "enem", "tujuh": "pitu", "delapan": "wolu", "sembilan": "songo", "sepuluh": "sepuluh"}
su_to_ja = {"hiji": "siji", "dua": "loro", "tilu": "telu", "opat": "papat", "lima": "limo", "genep": "enem", "tujuh": "pitu", "dalapan": "wolu", "salapan": "songo", "sapuluh": "sepuluh"}

def kamusIndoEnglish(id_to_en):
    number=input("Masukkan Nomor: ")
    for i in range (len(id_to_en)):
        if number in id_to_en:
            print (number, "=", id_to_en[number])
            i = input("Apakah anda ingin melanjutkan ? (y/n): ")
            if i == "y":
                return kamusIndoEnglish(id_to_en)
            if i == "n":
                print("Terima Kasih")
                break
    else:
        print("Tidak Ditemukan")
        i = input("Apakah anda ingin melanjutkan ? (y/n): ")
        if i == "y":
            return kamusIndoEnglish(id_to_en)

def kamusIndoSunda(id_to_su):
    number=input("Masukkan Nomor: ")
    for i in range (len(id_to_su)):
        if number in id_to_su:
            print (number, "=", id_to_su[number])
            i = input("Apakah anda ingin melanjutkan ? (y/n): ")
            if i == "y":
                return kamusIndoEnglish(id_to_su)
            if i == "n":
                print("Terima Kasih")
                break
    else:
        print("Tidak Ditemukan")
        i = input("Apakah anda ingin melanjutkan ? (y/n): ")
        if i == "y":
            return kamusIndoEnglish(id_to_su)

def kamusIndoJawa(id_to_ja):
    number=input("Masukkan Nomor: ")
    for i in range (len(id_to_ja)):
        if number in id_to_ja:
            print (number, "=", id_to_ja[number])
            i = input("Apakah anda ingin melanjutkan ? (y/n): ")
            if i == "y":
                return kamusIndoEnglish(id_to_ja)
            if i == "n":
                print("Terima Kasih")
                break
    else:
        print("Tidak Ditemukan")
        i = input("Apakah anda ingin melanjutkan ? (y/n): ")
        if i == "y":
            return kamusIndoEnglish(id_to_ja)

def kamusSundaJawa(su_to_ja):
    number=input("Masukkan Nomor: ")
    for i in range (len(su_to_ja)):
        if number in su_to_ja:
            print (number, "=", su_to_ja[number])
            i = input("Apakah anda ingin melanjutkan ? (y/n): ")
            if i == "y":
                return kamusIndoEnglish(su_to_ja)
            if i == "n":
                print("Terima Kasih")
                break
    else:
        print("Tidak Ditemukan")
        i = input("Apakah anda ingin melanjutkan ? (y/n): ")
        if i == "y":
            return kamusIndoEnglish(su_to_ja)

nomor = input("Pilih Kamus \n 1. Indonesia Inggris \n 2. Indonesia Sunda \n 3. Indonesia Jawa \n 4. Sunda Jawa \n Input :")
if nomor == "1":
    kamusIndoEnglish(id_to_en)
if nomor == "2":
    kamusIndoSunda(id_to_su)
if nomor == "3":
    kamusIndoJawa(id_to_ja)
if nomor == "4":
    kamusSundaJawa(su_to_ja)
