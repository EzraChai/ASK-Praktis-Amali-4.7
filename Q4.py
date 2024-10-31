def isipaduKuboid(panjang, lebar, tinggi):
    isipadu = panjang * lebar * tinggi
    print("Isi padu ialah ", isipadu, "\n")

def isipaduSilinder(jejari, tinggi):
    isipadu = 3.142 * jejari * jejari * tinggi
    print("Isi padu ialah ", isipadu, "\n")

def isipaduKon(jejari, tinggi):
    isipadu = 1 / 3.0 * 3.142 * jejari * jejari * tinggi
    print("Isi padu ialah ", isipadu, "\n")

def isipaduSfera(jejari):
    isipadu = 4.0/3 * 3.142 * jejari * jejari * jejari
    print("Isi padu ialah ", isipadu, "\n")


pilihan = -1

print("******************************")
print("    Menu Mengira Isi Padu     ")
print("******************************")
print("1. Kuboid\n2. Silinder\n3. Kon\n4. Sfera\n\n Masukkan 0 untuk menamatkan program.")
print("******************************")
pilihan = int(input("Masukkan pilihan anda: [0-4]: "))

while pilihan != 0:

    if pilihan == 1:
        panjang = int(input("Masukkan panjang : "))
        lebar = int(input("Masukkan lebar : "))
        tinggi = int(input("Masukkan tinggi : "))
        isipaduKuboid(panjang, lebar, tinggi)

    elif pilihan == 2:
        jejari = int(input("Masukkan jejari : "))
        tinggi = int(input("Masukkan tinggi : "))
        isipaduSilinder(jejari, tinggi)

    elif pilihan == 3:
        jejari = int(input("Masukkan jejari : "))
        tinggi = int(input("Masukkan tinggi : "))
        isipaduKon(jejari, tinggi)

    elif pilihan == 4:
        jejari = int(input("Masukkan jejari : "))
        isipaduSfera(jejari)
    else:
        print("Sila masukkan pilihan antara [0-4] sahaja.\n")

    pilihan = int(input("Masukkan pilihan anda: [0-4]: "))
        
