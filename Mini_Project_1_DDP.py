absensi = []

while True:
    print("\n------ Menu Absensi ------")
    print("1. Absen")
    print("2. Lihat Data Absensi")
    print("3. Ubah Data Absensi")
    print("4. Keluar")
    pilih = input("Pilih (1/2/3/4/5) : ")

    if pilih == "1":
        print("\nMasukkan Data Anda")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")

        data_absensi = (nama, nim, kehadiran)
        absensi.append(data_absensi)
        a = absensi[0]

        if kehadiran == "Izin":
            alasan = input("Izin apa = ")
            data_absensi = (nama, nim, kehadiran, alasan)
            absensi.append(data_absensi)
            a = absensi[0]
            print("\n| Data Kehadiran")
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("| Alasan    :", data_absensi[3])
            print("\nData Anda telah direkam")
            print("--------------------------")

        elif kehadiran == "izin":
            alasan = input("Izin apa = ")
            data_absensi = (nama, nim, kehadiran, alasan)
            absensi.append(data_absensi)
            a = absensi[0]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("| Alasan    :", data_absensi[3])
            print("\nData Anda telah direkam")
            print("--------------------------")

        else:
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nData Anda telah direkam")
            print("--------------------------")

    if pilih == "2":
        if kehadiran == "Izin":
            print("\n| Data Kehadiran",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("| Alasan    :", data_absensi[3])
        # elif kehadiran == "izin":
        #     print("\n| Data Kehadiran", nama)
        #     print("| Nama      :", a[0])
        #     print("| NIM       :", a[1])
        #     print("| Kehadiran :", a[2])
        #     print("| Alasan    :", data_absensi[3])
        #     print(" ")
        else:
            print("\n| Data Kehadiran")
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])

    elif pilih == "3":
        print("\nUbah Data")
        print("---------------")
        nama = input("\nMasukkan Nama = ")
        nim = input("Masukkan NIM = ")
        kehadiran = input("(Hadir/Sakit/Izin/Alpa) = ")
        if kehadiran == "Izin":
            alasan = input("Izin apa = ")
            data_absensi = (nama, nim, kehadiran, alasan)
            absensi.append(data_absensi)
            a = absensi[0]
            print("\n| Data Kehadiran")
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("| Alasan    :", data_absensi[3])
            print("\nPerubahan Data Anda telah direkam")
            print("------------------------------------")

        elif kehadiran == "izin":
            alasan = input("Izin apa = ")
            data_absensi = (nama, nim, kehadiran, alasan)
            absensi.append(data_absensi)
            a = absensi[0]
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("| Alasan    :", data_absensi[3])
            print("\nPerubahan Data Anda telah direkam")
            print("------------------------------------")

        else:
            print("\n| Data Kehadiran ",)
            print("| Nama      :", a[0])
            print("| NIM       :", a[1])
            print("| Kehadiran :", a[2])
            print("\nPerubahan Data Anda telah direkam")
            print("------------------------------------")

    # elif pilih == "4":
    #     hapus = input("Hapus data absensi mahaasiswa? (ya/tidak)")
    #     if hapus == "ya":
    #         absensi.pop(0)
    #         print("Data berhasil dihapus")
    #     elif hapus == "tidak":
    #         print("Data tidak jadi dihapus")
    #     else:
    #         print("Jawaban anda tidak valid")

    elif pilih == "4":
        print("\nKembali lagi nanti!")
        print(" ")
        break

    # update = input("\nIngin Merubah Data? (ya/tidak) : ")
    # if update == "ya":
        

    # elif update == "tidak":
    #     print("")

    



