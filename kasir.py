import numpy as np 
import pandas as pd 
import csv 

def buat_csv():
    data_awal = open('kasir.csv', "w")
    data_awal.write(
        "NAMA PELANGGAN\t, NAMA PAKET\t, TOTAL BAYAR\n")
    data_awal.close()

# pengolahan data
class Cashier():
    jumlah_pelanggan = 0

    def __init__(self):
        print("="*50, 'SELAMAT DATANG DI TOKO MIRZA', "="*50)
        pool_kode_paket = ["A","B","C"]
        pool_nama_paket = ["Whitening","Acne","Anti Aging"]
        pool_harga = ["Rp 500.000","Rp 700.000","Rp 1.000000"]
        print('-'*60)
        print('|KODE PAKET\t', '|NAMA PAKET\t\t', '|HARGA\t\t\t|')
        print('-'*60)
        for x,y,z in zip(pool_kode_paket,pool_nama_paket,pool_harga):
            print("|", x, '\t\t' , "|", y, '\t\t' , "|", z)
        print('-'*60)
        print('\n\n')
        self.input_data()

    def input_data(self):
        # input data dari pelanggan
        self.nama_pelanggan = input(str('Masukkan nama anda : '))
        self.kode_pelanggan = input(str('Masukkan kode pelanggan [x/y]: '))
        self.kode_paket = input(str('Masukkan nama kode paket [A/B/C]: '))
        self.jumlah_beli = int(input('Masukkan jumlah unit yang dibeli: '))
        print('\n\n')
        self.olah_data()

    def olah_data(self):
        # harga sesuai kode paket
        self.harga_awal = 0
        if self.kode_paket == 'A' or 'a': 
            self.harga_awal += 500000
        elif self.kode_paket == "B" or 'b':
            self.harga_awal += 700000
        else:
            self.harga_awal += 1000000
        
        # harga setelah dikali jumlah pembelian
        self.total_bayar = int(self.harga_awal) * int(self.jumlah_beli)

        # harga setelah dipotong member
        if self.kode_pelanggan == "x": 
            self.total_bayar = int(self.total_bayar * 90 / 100)
        else:
            self.total_bayar = int(self.total_bayar * 1)
        self.show_info()

    def show_info(self):
        print('='*60)
        print('NAMA PELANGGAN\t', 'JENIS PELANGGAN\t', 'NAMA PAKET\t', 'JUMLAH BELI\t', 'TOTAL BAYAR')
        print('='*60)
        print("{}\t\t {}\t\t\t {}\t\t {}\t\t {}".format(self.nama_pelanggan, self.kode_pelanggan, self.kode_paket, self.jumlah_beli, self.total_bayar))
        self.make_history()
    
    def make_history(self):
        data = open('kasir.csv', "a")
        data.write("{},{},{}".format(self.nama_pelanggan, self.kode_paket, str(self.total_bayar)))
        data.write('\n')
        data.close()

Cashier()
