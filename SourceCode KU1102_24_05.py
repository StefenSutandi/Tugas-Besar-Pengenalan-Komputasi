#Program Lift
import time
import random

#Program catudaya
def daya(): # checked
    b = 0
    w = 'False'
    while(w == 'False' and b < 3):
        a = str(input("Catudaya(On/Off)?:True/False -=> "))
        if(a == w):
            print("Lift mati")
            b += 1
        elif(a == 'True'):
            print("~~~Lift sedang dihidupkan dayanya~~~")
            w = 'True'
            break
        else:
            print("Syntax ERROR")
            b += 1
    return w

#Program masukkan nomor lantai
def nomorLantai(i,a):#a = jlhLantai (checked)
    for j in range(0,a):
        N[i] = str(j+1)
        i += 1
    return

#Program tujuan lift 
def naik_turun(): #lantai naik atau turun
    if arahLift[0] == False :
        print("**********PINTU TERTUTUP**********")
        lantaiSekarang1 = lantaiSekarang - 1
        print(f"Lift turun ke lantai {lantaiSekarang1}")
        for i in range(3):
            time.sleep(2)
            print(">",end="")
        print()
        print(f"Lift tiba di lantai {lantaiSekarang1}")
        print("**********PINTU TERBUKA**********")
        return lantaiSekarang1
    else: # arahLift() == True
        print("**********PINTU TERTUTUP**********")
        lantaiSekarang1 = lantaiSekarang + 1
        print(f"Lift naik ke lantai {lantaiSekarang1}")
        for i in range(3):
            time.sleep(2)
            print(">",end="")
        print()
        print(f"Lift tiba di lantai {lantaiSekarang1}")
        print("**********PINTU TERBUKA**********")
        return lantaiSekarang1

#Program arah lift
def arahLift():
    arahLift1 = arahLift
    if(lantaiSekarang == jlhLantai or lantaiSekarang == 1):
        arahLift1 = not(arahLift[0])
    return arahLift1
#Program hilangkan tombol tamu pas berada di lantai itu
def tujuanLift():
    i = 0
    while(i <= tamuMax and tamu[i] != 0):
        if(tamu[i] == lantaiSekarang):
            tamu[i] = 0
        i += 1
    return

'''
TC:
nomorLantai(i,jlhLantai)
print(N)
'''
# Input fungsi berat total lift
def Entry(i):#checked
    Total = People[i]
    LiftTotalWeight = Total 
    return Total

#saat lift kelebihan orang
def lebihOrang():#
    jlhTamu1 = jlhTamu
    orangOut = 0
    while(jlhTamu1 > tamuMax):
        print("====================================================")
        print("Kelebihan jumlah orang!")
        orangOut = int(input("Masukkan jumlah orang yang keluar: "))
        jlhTamu1 -= orangOut
    return orangOut

# Input fungsi berat masing - masing penumpang    
def people():
    a = 0# Acuan untuk kelebihan
    if totalBerat > LoadLift :
        if(totalBerat > LoadLift):
            print("====================================================")
            print("Kelebihan berat beban!")
            a += 1
        #People[i] = int(input("Masukkan kembali berat penumpang: "))
    return a

#Program keluarkan tamu
def keluarkan(people):#checked
    keluar = 0
    totalBerat1 = totalBerat - keluar
    while(totalBerat1 > LoadLift and people > 0):
        keluarOrang()
        keluar = keluarBerat()
        totalBerat1 -= keluar
    return keluar

#Program untuk orang yang keluar
def keluarOrang():#checked
    orangOut = int(input("Masukkan jumlah orang yang keluar: "))
    return orangOut

#Program keluar berat orang
def keluarBerat():#checked
    h = 0
    keluarB = 0
    o = 0
    keluar = 2
    while(o < keluar and keluar <= tamuMax):
        beratOut = float(input("Masukkan berat yang dikeluarkan: "))
        for k in range(tamuMax):
            h = 0
            if(People[k] == beratOut):
                People[k] = 0
                print(People)
                break
            else:
                h += 1
            if(h == tamuMax):
                beratOut = float(input("Masukkan ulang berat yang ingin dikeluarkan: "))
        o += 1
        keluarB += beratOut
    h = 0
    o = 0
    return keluarB


#Program jumlah tamu di lift tidak termasuk masuk
def tamuLift(banyakTamu):#checked
    keluar = int(input("Jumlah Tamu yang keluar lift: "))
    jlhTamu1 = jlhTamu - keluar
    return jlhTamu1

'''
LiftWeight = 300
LoadLift = 1300
totalBerat = 0
People = [0 for i in range(10)]
masuk = int(input("Masukkan jumlah tamu yang masuk: "))
for i in range(0, masuk):
    People[i] = int(input("Masukkan berat (kg) orang ke-"+ str(i+1)+ ": "))
    totalBerat = Entry()
People(keluarkan())


''
jlhTamu = tamuLift(jlhTamu)
'''

#Program check symbol atau angka
def check(tombolyangditekan): #checked
    c = 0
    for i in range(0,jlhLantai):
        if(N[i] == tombolyangditekan):
            c += 1
    return c

#Program jenis tombol
def tombol(n): #checked
    print()
    print("|/\Petunjuk/\|")
    for j in range(i,n):#n = jumlah lantai gedung
        print("Tekan/ketik "+str(j+1)+"          -> ke Lantai "+str(j+1))
    time.sleep(1)
    print()
    print("Tombol lainnya")
    print("Tekan/ketik ?          -> ~Bantuan~ ")
    print("Tekan/ketik power      -> catudaya lift ")
    print("Tekan/ketik ok         -> Tombol lantai yang ingin dituju telah ditekan")
    print("Tekan/ketik cancel     -> Fungsi pembatalan tombol ")
    print("Tombol yang telah di tekan :",tamu)
    return

#Program Tombol yang di tekan Tamu
def tekanTombol(Angkayangditekan,b,c):#checked
    #a diisi tombol yang di tekan
    #b diisi dengan tombol angka
    #c diisi dengan Tombol Symbol
    #a = input("Tombol yang ingin ditekan ~silahkan di ketik~ :")
    if(len(Angkayangditekan) == 1):
        return b
    else:
        return c
'''
a = '1'
b = '?'
print(tekanTombol(a,1,'salah'))
print(tekanTombol(b,1,'salah'))
'''
#Program setelan tombol Angka
def tombolAngka(a): # Checked
    b = 0
    c = 0
    i = 0
    d = 0
    while(i< tamuMax or b == 1):
        for j in range(0,tamuMax):
            if(tamu[j] == a):
                tamu[j] = 0
                c += 1
        if(tamu[i] == 0 and c == 0 and AatauS != 0):
            tamu[i] = a
            b += 1# break
            break
        else:
            i += 1
    return
'''
tamu[0] = 1
a = 2
tombolAngka(a)
#tamu[tombolAngka(2)] = a
'''


#Program setelan tombol Sybmbol
def tombolSymbol(a):# checked
    if(a == "?"): # percabangan bantuan
        print("Tolong Katakan bantuan yang dapat kami selesaikan?")
        masalah = str(input("Jawab :"))
        print("Mohon ditunggu, Masalah mu akan kami proses",end="")
        for i in range(0,10):
            time.sleep(2)
            print(".")
        print("Terima kasih atas kesabarannya, masalah mu telah kami proses")
        print("Mohon ditunggu penyelesaiannya")
        return
    elif(a == "ok"): # percabangan tombol berulang
        print("~Terdata~")
        return
    elif(a == "power"): # percabangan power
        w = str(input("On(True)/Off(False) -->"))
        if(w == 'True'):
            print("Lift sedang hidup ")
        elif(w == 'False'):
            print("~Lift akan dimatikan~")
            print("~Harap kosongkanlift~")
            for i in range(7):
                print(".")
                time.sleep(1)
            return w
    elif(a == 'cancel'):
        b = int(input("Nomor Lantai yang ingin dibatalkan: "))
        for j in range(0,jlhTamu):
            #tombol yang ditekan oleh seorang tamu
            if(b == tamu[j]):
                tamu[j] = 0
        return

#Program Lift saat awal /posisi lift dan saat semua tamu di dalam lift kosong
def PanggilLift(Lantai):#checked
    LantaiSekarang = int(input("Masukkan lantai yang tombolnya ditekan: "))
    while(LantaiSekarang > jlhLantai or LantaiSekarang <= 0):
        print("Jangan Usil! Gedung ini tidak melebihi lantai "+str(jlhLantai))
        LantaiSekarang = int(input("Masukkan lantai yang tombolnya ditekan lagi: "))
    print("Posisi Lift sekarang di : Lantai "+str(Lantai))
    while Lantai!=LantaiSekarang:
        print("Lantai "+str(Lantai),end="")
        if Lantai<LantaiSekarang:
            Lantai+=1
            for delay in range(3):
                print('-',end='')
                time.sleep(1)
            print(">",end=" ")
            print('Lantai', Lantai)
        else:
            Lantai-=1
            for delay in range(3):
                print('-',end='')
                time.sleep(1)
            print(">",end=" ")
            print('Lantai', Lantai)
    else:
        print("Ding",end="")
        for delay in range(3):
            print('~', end='')
        print()
        print('Lantai',LantaiSekarang)
        print('\n===== Pintu Lift terbuka =====')
    return LantaiSekarang

#Program tombol ditekan berulang
def tombolBerulang(tombolTamu):#checked
    for j in range(0,jlhTamu):
        #tombol yang ditekan oleh seorang tamu
        if(tombolTamu == tamu[j]):
            tamu[j] = 0
    return tamu

#tombol yang ditekan tamu saat berada di lantai itu
def hilangkan():#
    for i in range(tamuMax):
        if(tamu[i] == str(lantaiSekarang)):
            tamu[i] = 0
    return

#Program saat lift kosong
def liftKosong():
    v = 0
    for i in range(tamuMax):
        if(tamu[i] == 0):
            v += 1
    if(v == tamuMax):
        kosong[0] = not(kosong[0])
        print("~Lift akan dimatikan~")
        print("~Harap kosongkanlift~")
        for i in range(7):
            print(".")
            time.sleep(1)
    return
        
'''
TC
tamu[0] = 1
tamu[1] = 2
tamu[2] = 8
a = 8
tombolBerulang(a)
print(tamu)
'''
print("Program lift version 4.4")
print("Program Lift ini merupakan versi SEDERHANA dari Program Lift Sebenarnya")
print("Jadi setiap tombol hanya dapat diketik")
print("Pesan dari tim 5: Maaf jika ada yang error saat di lakukan")
print("Akhir Kata      : Selamat menikmati program ini")
for qq in range(2):
    time.sleep(1)
print("Starting Program",end="")
for ii in range(3):
    print(".",end="")
print()
time.sleep(2)
print("=========================== PROGRAM LIFT =======================================")

w = daya()
print("loading",end="")
''
for m in range(0,8):
    print("~",end="")
    time.sleep(2)
''
print()
print("Kapasitas maksimal lift adalah 1000 kg.")
#global variable
jlhLantai = int(input("Masukkan jumlah lantai gedung ini: "))
jlhTamu = 0
tamuMax = 15
Lantai = random.randint(1,jlhLantai)
arahLift = [True] # Saat True = naik ; False = turun
People = [0 for i in range(tamuMax)]# berat masing-masing tamu
N = [0 for i in range(jlhLantai)] #nomor lantai
tamu = [0 for j in range(tamuMax)] #Tombol yang ditekan Tamu
i = 0 # lantai acuan/range dari jumlah tamu
kosong = [False] #False = ada orang , True = tidak ada orang
buka = ['P','i','n','t','u',' ','L','i','f','t',' ','D','i','b','u','k','a']
tutup = ['P','i','n','t','u',' ','L','i','f','t',' ','D','i','t','u','t','u','p']
AatauS = 0 # Acuan untuk tentuakn angka atau symbol
nomorLantai(i,jlhLantai)
print()
lantaiSekarang = PanggilLift(Lantai)
print()
LiftWeight = 300
LoadLift = 1300
totalBerat = 300

''
while(w != 'False' and kosong[0] == False):
    tujuanLift()
    ''
    for z in range(0,17):
        print(buka[z],end="")
        time.sleep(0.8)
    ''
    hilangkan()
    print()
    print('Status :')
    print("Lift sedang bergerak ",end="")
    if(arahLift[0] == True):
        print("naik")
    else: #(arahLift[0] == 'False'):
        print("turun")
    print('/nJumlahTamu: ',jlhTamu)
    print('/nLantai Sekarang: ',lantaiSekarang)
    print('/nBerat masing-masing tamu: ',People)
    print('/nNomor Yang ditekan Tamu: ',tamu)
    #Berat
    masuk = int(input("Jumlah Tamu yang masuk lift: "))
    keluar = int(input("Masukkan jumlah orang yang keluar: "))
    h = 0
    keluarB = 0
    o = 0 
    while(o < keluar and keluar <= tamuMax):
        beratOut = float(input("Masukkan berat yang dikeluarkan: "))
        for k in range(tamuMax):
            h = 0
            if(People[k] == beratOut):
                People[k] = 0
                print(People)
                break
            else:
                h += 1
            if(h == tamuMax):
                beratOut = float(input("Masukkan ulang berat yang ingin dikeluarkan: "))
        o += 1
        keluarB += beratOut
    h = 0
    o = 0
    jlhTamu += (masuk - keluar)
    jlhTamu -= int(lebihOrang())
    z = 0
    b1 = 0
    while(z < masuk):
        for b in range(tamuMax):
            if(People[b] == 0):
                b1 = b
                break
        People[b1] = float(input("Masukkan berat (kg) orang ke-"+ str(z+1)+ ": "))
        totalBerat += Entry(b1)
        z += 1
        if(z == masuk):
            break
        #print(totalBerat)
    z = 0
    b1 = 0
    print(People)
    totalBerat -= (keluarkan(people()) + keluarB) 

    print("Total Berat saat ini(dalam kg): ",totalBerat)
    # Bagian tombol
    tombol(jlhLantai)
    #print(jlhTamu)
    while(masuk > 0 and w != 'False'):
        a = input("Tombol yang ingin ditekan ~silahkan di ketik~ :")
        AatauS = check(a)
        for k in range(0,tamuMax):
            if(tamu[k] == a):
                tombolBerulang(a)
                #print(tamu)
                break
            elif(tamu[k] != a and tamu[k] == 0):
                w = tekanTombol(a,tombolAngka(a),tombolSymbol(a))
                #print(tamu)
                break
            #print(w)
        masuk -= 1
        ''
        if(w == 'False'):
            break
        ''
    AatauS = 0

    #Tambahan
    ''
    for q in range(0,18):
        print(tutup[q],end="")
        time.sleep(0.8)
    for t in range(0,5):
        print(".",end="")
    ''
    print()
    print()
    liftKosong()
    if(w != 'False' and kosong[0] == False):
        if(lantaiSekarang == jlhLantai or lantaiSekarang == 1):
            arahLift[0] = not(arahLift[0])
        lantaiSekarang = naik_turun()

print("Lift dimatikan")
print("Loading",end="")
for g in range(0,8):
    print("..",end="")
    time.sleep(3)
print()
print("Off")

''
