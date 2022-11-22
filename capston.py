
daftarsiswa=[
        {
            'Nomor Induk Siswa':(12345),
            'Nama':'Adhyaksa',
            'Nilai Matematika':90,
            'Nilai IPA':85,
            'Nilai IPS':100,
        },
        {
            'Nomor Induk Siswa':(21345),
            'Nama':'Agung',
            'Nilai Matematika':85,
            'Nilai IPA':75,
            'Nilai IPS':60,
        },
        {
            'Nomor Induk Siswa':(23145),
            'Nama':'Bono',
            'Nilai Matematika':97,
            'Nilai IPA':66,
            'Nilai IPS':82,
        },
        {
            'Nomor Induk Siswa':(23415),
            'Nama':'Faruq',
            'Nilai Matematika':90,
            'Nilai IPA':85,
            'Nilai IPS':100,
        },
        {
            'Nomor Induk Siswa':(23451),
            'Nama':'Wuilly',
            'Nilai Matematika':100,
            'Nilai IPA':88,
            'Nilai IPS':70,
        }
    ]

def menampilkandaftarsiswa():
    print('\nMenu Daftar Nilai Siswa\n')
    pilihan1=input('''
    1. Tampilkan Seluruh Data Nilai Siswa
    2. Pencarian Data Nilai Siswa
    3. Kembali ke Menu Awal
    
    Silahkan Ketik Angka Menu yang ingin dipilih: ''')
    if (pilihan1=='1'):
        print('Berikut Data Lengkap Daftar Nilai Siswa')
        for i in range(len(daftarsiswa)):
            print('NIS:{}\t Nama:{}\t Nilai Matematika:{}\t Nilai IPA:{}\t Nilai IPS:{}'.format(daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
        print('\nMenu Daftar Nilai Siswa\n')
        pilihan1=input('''
        1. Tampilkan Seluruh Data Nilai Siswa
        2. Pencarian Data Nilai Siswa
        3. Kembali ke Menu Awal
    
        Silahkan Ketik Angka Menu yang ingin dipilih: ''')
    elif(pilihan1=='2'):
        pilihan1ke2 = input('Silahkan Masukan Nomor Induk Siswa dari Data Siswa yang ingin dicari: ')
        for i in range(len(daftarsiswa)):
            dsiswa = daftarsiswa[i]['Nomor Induk Siswa']
            if(dsiswa==int(pilihan1ke2)): 
                print('\nBerikut Hasil Pencarian:\n')
                print('NIS:{}\t Nama:{}\t Nilai Matematika:{}\t Nilai IPA:{}\t Nilai IPS:{}'.format(daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
            else:
                menampilkandaftarsiswa()
    elif(pilihan1=='3'):
        main()

def menambahdatanilaisiswa():
    print('\nMenu Membuat Data Nilai Siswa\n')
    pilihan1=input('''
    1. Membuat Data Nilai Siswa
    2. Kembali ke Menu Awal
    
    Silahkan Ketik Angka Menu yang ingin dipilih: ''')
    if(pilihan1=='1'):
        nomornis=input('Masukan 5 Angka Nomor Induk Siswa: ')
        for i in range(len(daftarsiswa)):
            nisbaru=daftarsiswa[i]['Nomor Induk Siswa']       
            if (nisbaru==int(nomornis)):
                print('Data Sudah Ada')
                menambahdatanilaisiswa()
        namasiswa=input('Masukan Nama Siswa: ')
        nilaimtk=input('Masukan Nilai Matematika Siswa: ')
        nilaiipa=input('Masukan Nilai IPA Siswa: ')
        nilaiips=input('Masukan Nilai IPS Siswa: ')
        daftarsiswa.append({
                'Nomor Induk Siswa':nomornis,
                'Nama':namasiswa,
                'Nilai Matematika':nilaimtk,
                'Nilai IPA':nilaiipa,
                'Nilai IPS':nilaiips,
            })
        print('Berikut Data yang akan ditambahkan: ')
        print('NIS:{}\t Nama:{}\t Nilai Matematika:{}\t Nilai IPA:{}\t Nilai IPS:{}'.format(nomornis,namasiswa,nilaimtk,nilaiipa,nilaiips))
        pertanyaan=input("Ketika 'Ya' untuk menyimpan data: ")
        if(pertanyaan=='Ya'):
            print('Data Berhasil Disimpan\n')
            menambahdatanilaisiswa()
    elif(pilihan1=='2'):
        main()
    else:
        menambahdatanilaisiswa()
   
def mengupdatenilaisiswa():
    print('\nMenu Memperbaharui Data Nilai Siswa\n')
    pilihan1=input('''
    1. Perbaharui Data Nilai Siswa
    2. Kembali ke Menu Awal
    
    Silahkan Ketik Angka Menu yang ingin dipilih: ''')
    if(pilihan1=='1'):
        nomornis=input('Masukan 5 Angka Nomor Induk Siswa: ')
        for i in range(len(daftarsiswa)):
            nisbaru=daftarsiswa[i]['Nomor Induk Siswa']       
            if (nisbaru!=int(nomornis)):
                print('Data yang Anda cari tidak ada')
                mengupdatenilaisiswa()
            else:
                print('NIS:{}\t Nama:{}\t Nilai Matematika:{}\t Nilai IPA:{}\t Nilai IPS:{}'.format(daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
                opsi2=input('Ketik "Ya" untuk lanjut perbaharui Data:')
                if(opsi2=='Ya'):
                    nilaiupdate=input('Masukan Nilai Baru: ')
                    pelajaran=input('''Daftar Pelajaran
                    1. Matematika
                    2. IPA
                    3. IPS
                    Masukan Mata Pelajaran Yang Ingin Diganti: ''')
            
                    if(pelajaran=='1'):
                            daftarsiswa[i]['Nilai Matematika':int(nilaiupdate)]
                            konfirmasi=input('Ketik "Ya" untuk perbaharui Data: ')
                            if(konfirmasi=='Ya'): print('Pembaharuan Data Anda Berhasil\n')
                            else: mengupdatenilaisiswa()
                    elif(pelajaran=='2'):
                            daftarsiswa[i]['Nilai IPA':int(nilaiupdate)]
                            konfirmasi=input('Ketik "Ya" untuk perbaharui Data: ')
                            if(konfirmasi=='Ya'): print('Pembaharuan Data Anda Berhasil\n')
                            else: mengupdatenilaisiswa()
                    elif(pelajaran=='3'):
                            daftarsiswa[i]['Nilai IPS':int(nilaiupdate)]
                            konfirmasi=input('Ketik "Ya" untuk perbaharui Data: ')
                            if(konfirmasi=='Ya'): print('Pembaharuan Data Anda Berhasil\n')
                            else: mengupdatenilaisiswa()               
                    
                else:
                    mengupdatenilaisiswa()
    elif(pilihan1=='2'):
        main()
    else:
        menambahdatanilaisiswa()

def menghapusnilaisiswa():
    print('\nMenu Menghapus Data Nilai Siswa\n')
    pilihan1=input('''
    1. Hapus Data Nilai Siswa
    2. Kembali ke Menu Awal
    
    Silahkan Ketik Angka Menu yang ingin dipilih: ''')
    if(pilihan1=='1'):
        nomornis=input('Masukan 5 Angka Nomor Induk Siswa: ')
        for i in range(len(daftarsiswa)):
            nisbaru=daftarsiswa[i]['Nomor Induk Siswa']       
            if (nisbaru!=int(nomornis)):
                print('Data yang Anda cari tidak ada')
                menghapusnilaisiswa()
            else:
                opsi2=input('Ketik "Ya" untuk lanjut hapus Data:')
                if(opsi2=='Ya'):
                    del daftarsiswa[i]
                    print('Penghapusan Data Anda Berhasil\n')
                    menghapusnilaisiswa()
                else: menghapusnilaisiswa()
    elif(pilihan1=='2'):
        main()
    else:
        menghapusnilaisiswa()
def main():
    pilihan =input('''
        Menu Program Akademik Scores - Nilai Siswa Kelas 7

        1. Daftar Nilai Siswa
        2. Input Nilai Siswa
        3. Perbaharui Nilai Siswa
        4. Hapus Nilai Siswa
        5. Keluar Program

        Silahkan Ketik Angka Menu yang ingin dipilih: ''')
    if(pilihan=='1'):
            menampilkandaftarsiswa()
    elif(pilihan=='2'):
            menambahdatanilaisiswa()
    elif(pilihan=='3'):
            mengupdatenilaisiswa()
    elif(pilihan=='4'):
            menghapusnilaisiswa()       

main() 
        


    # if  (pilihan == str(1)):
    #     print('Daftar Siswa\n')
    #     print('No.\t NIS\t Nama\t Nilai Matematika\t Nilai IPA\t Nilai IPS')
    #     for i in range(len(daftarsiswa)):
    #         print('{}\t {}\t {}\t {}\t {}'.format(i,daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
    # elif(pilihan==str(2)):
    #     nomornis=input('Masukan Nomor Induk Siswa: ')
    #     namasiswa=input('Masukan Nama Siswa: ')
    #     nilaimtk=input('Masukan Nilai Matematika Siswa: ')
    #     nilaiipa=input('Masukan Nilai IPA Siswa: ')
    #     nilaiips=input('Masukan Nilai IPS Siswa: ')
    #     daftarsiswa.append({
    #         'Nomor Induk Siswa':nomornis,
    #         'Nama':namasiswa,
    #         'Nilai Matematika':nilaimtk,
    #         'Nilai IPA':nilaiipa,
    #         'Nilai IPS':nilaiips,
    #     })
    #     print('Penambahan Data Anda Berhasil\n')
    #     print('Daftar Siswa\n')
    #     print('No.\t Nama\t Nilai Matematika\t Nilai IPA\t Nilai IPS')
    #     for i in range(len(daftarsiswa)):
    #        print('{}\t {}\t {}\t {}\t {}'.format(i,daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
    # elif(pilihan==str(3)):
    #     nomornis=input('Masukan Nomor Induk Siswa: ')
    #     nilaiupdate=input('Masukan Nilai Baru: ')
    #     pelajaran=input('Masukan Mata Pelajaran Yang Ingin Diganti: ')
    #     if(pelajaran=='Matematika'):
    #         daftarsiswa[nomornis]['Matematika':nilaiupdate]
    #     elif(pelajaran=='IPA'):
    #         daftarsiswa[nomornis]['IPA':nilaiupdate]
    #     elif(pelajaran=='IPS'):
    #         daftarsiswa[nomornis]['IPS':nilaiupdate]
    #     print('Pembaharuan Data Anda Berhasil\n')
    #     print('Daftar Siswa\n')
    #     print('No.\t Nama\t Nilai Matematika\t Nilai IPA\t Nilai IPS')
    #     for i in range(len(daftarsiswa)):
    #         print('{}\t {}\t {}\t {}\t {}'.format(i,daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
    # elif(pilihan==str(4)):
        # nomornis=input('Masukan Nomor Induk Siswa: ')
        # hapusnilai=input('Masukan Nilai Baru: ')
        # pelajaran=input('Masukan Mata Pelajaran Yang Ingin Diganti: ')
    #     print('Daftar Siswa\n')
    #     print('No.\t Nama\t Nilai Matematika\t Nilai IPA\t Nilai IPS')
    #     for i in range(len(daftarsiswa)):
    #         print('{}\t {}\t {}\t {}\t {}'.format(i,daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
    #     nomordata=input('Masukan Nomor Nilai yang Ingin Dihapus: ')
    #     del daftarsiswa[nomordata]
    #     print('Daftar Siswa\n')
    #     print('No.\t Nama\t Nilai Matematika\t Nilai IPA\t Nilai IPS')
    #     for i in range(len(daftarsiswa)):
    #         print('{}\t {}\t {}\t {}\t {}'.format(i,daftarsiswa[i]['Nomor Induk Siswa'],daftarsiswa[i]['Nama'],daftarsiswa[i]['Nilai Matematika'],daftarsiswa[i]['Nilai IPA'],daftarsiswa[i]['Nilai IPS']))
    # elif(pilihan==str(5)):
    #     print('Anda Sudah Keluar dari Program, terima kasih!')
    # break