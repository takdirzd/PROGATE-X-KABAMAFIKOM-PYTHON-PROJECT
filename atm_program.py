import random
import datetime
from customer import customer

atm = customer(id)

while True:  #looping pemeriksaan
    id = int(input("Masukkan Pin = "))
    trial = 0
    trialb = 0

    while (id != atm.checkcustpin() and trial < 3):    #looping pemeriksaan pin dan batas 3 x percobaan jika gagal
        id = int(input("pin yang anda masukkan salah. silahkan masukkan lagi:"))
        trial += 1
        if (trial == 3):
            print("Program Error")
            exit()

    while True:   #Looping Utama
        print("===========Selamat Datang di ATM=============")
        print("Menu Pilihan \n 1. Cek Saldo \n 2. Debet \n 3. Simpan \n 4. Ganti Pin \n 5. Keluar")
        inputmenu = int(input("Masukkan pilihan : "))

        if (inputmenu == 1):
            print("+++Saldo anda sebesar ", "Rp.",str(atm.checkcustbalance())," +++")

        elif (inputmenu == 2):
            nominal = float(input("Masukkan nominal saldo : "))
            verify_withdraw = input("Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y / n   " + str(nominal) + " ")
            if verify_withdraw == "y":
                print("Saldo awal anda adalah: ", "Rp. ",atm.checkcustbalance())
            else:
                break

            if nominal < atm.checkcustbalance():
                atm.withdrawbalance(nominal)
                print("Transaksi Berhasil!!")
                print("Sisa saldo anda sebesar: ","Rp. ",atm.checkcustbalance())
            else:
                print("Maaf! Saldo anda tidak mencukupi!")
                print("Silahkan melakukan penambahan nominal saldo")

        elif (inputmenu == 3):
            nominal = float(input("Masukkan nominal saldo : "))
            verify_withdraw = input("Apakah anda akan menyimpan dengan nominal berikut? Y/N  "+ str(nominal)+ ' ')
            if verify_withdraw == "y":
                atm.depositbalance(nominal)
                print("Saldo anda sekarang adalah: ", "Rp. " + str(atm.checkcustbalance())+ '\n')
            else:
                break

        elif (inputmenu == 4):
            verify_pin = int(input("Masukkan pin anda :"))
            while verify_pin != int(atm.checkcustpin()):
                verify_pin= int(input("pin yang anda masukkan salah. silahkan masukkan lagi:"))
                trialb += 1
                if (trialb == 3):
                    print("Program Error")
                    exit()

            updated_pin = int(input("silakan masukkan pin baru: "))

            print("pin anda berhasil diganti!")
            verify_newpin = int(input("coba masukkan pin baru: "))

            if verify_newpin == updated_pin:
                print("Pin baru berhasil")

            else:
                print("Pin yang anda masukkan salah")



        elif (inputmenu == 5):
            print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
            print("No. Record :", random.randint(100000, 1000000))
            print("Tanggal: ", datetime.datetime.now())
            print("Saldo akhir: ", atm.checkcustbalance())
            print("Terima kasih telah menggunakan ATM !")
            exit()

        else:
            print("Error, maaf, menu tidak tersedia")




