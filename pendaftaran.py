import numpy as np
# function pilihan
def daftar():
    inputawal = input("keyword :")
    if inputawal == "yes" :
        Student()
    elif inputawal == "no" :
        print("good luck")
    else:
        daftar()

# function input data
class Student():
    total = list(n for n in range(100))
    users = 0
    def __init__(self):
        self.name = str(input("Enter your name "))
        self.uname = str(input("Enter your username "))
        self.age = int(input("Enter your age ")) 
        self.number = self.total[self.users + 1]
        daftar_siswa = open("daftar_siswa.txt", "a")
        daftar_siswa.write("\n\nData :\n Nama\t: {} \nUname\t: {}  \nAge\t\t: {} \n\n".format(self.name,self.uname,self.age))
        daftar_siswa.close()
        self.getpassword()

    def getinfo(self):
        data = [self.name, self.uname, self.age, self.number]
        jenis_data = ["NAME", "USERNAME", "AGE","NUMBER"]
        print("\nYour data :",)
        for x,y in zip(jenis_data, data):
            print(x, "\t\t:" , y)

    def getpassword(self):
        self.getinfo()



# surface
print("="*50, "PENDAFTARAN TELAH DIBUKA", "="*50,"\n")

print("What do you need ?")
print("press 'yes' you wanna join")
print("press 'no' if you wanna exit")
daftar()





    




