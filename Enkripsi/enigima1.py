#Import Library
from enigma.machine import EnigmaMachine

print(" ")
print("===Masukan Pilihan===")
print("1. Ke Chiper")
print("2. Ke Plain")
print("=====================")
print(" ")
pil = int(input("Masukan Pilihan: "))


def kechiper():
    #Memasukan Text
    print(" ")
    a = str(input("Input Text: "))

    #Pengaturan Mesin (Dapat Diubah)
    machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',
    reflector='B',
    ring_settings=[1, 20, 11],
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

    #Menerjemahkan ke Chiper
    machine.set_display('WXC')

    msg_key = machine.process_text('KCH')

    machine.set_display(msg_key)

    plaintext = a
    chipertext = machine.process_text(plaintext)

    print(" ")

    print("Hasil:",chipertext)


def keplain():
    #Memasukan ChiperText
    print(" ")
    a = str(input("Input ChiperText: "))

    #Pengaturan Mesin (Dapat Diubah)
    machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',
    reflector='B',
    ring_settings=[1, 20, 11],
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

    #Menerjemahkan ke Plaintext
    machine.set_display('WXC')

    msg_key = machine.process_text('KCH')

    machine.set_display(msg_key)

    chipertext = a
    plaintext = machine.process_text(chipertext)

    #PlainText Diolah Agar Menjadi lebih terbaca
    x = plaintext.replace("X", " ")
    y = x.capitalize()

    #Print Hasil akhir
    print(" ")
    print("Hasil:",y)
    print(" ")


if pil == 1:
    kechiper()

elif pil == 2:
    keplain()

else:
    print(pil,"Tidak Ada Dalam Pilihan")


while True:
    print(" ")
    print("===Masukan Pilihan===")
    print("1. Ke Chiper")
    print("2. Ke Plain")
    print("98. Keluar")
    print("=====================")
    print(" ")
    pil = int(input("Masukan Pilihan: "))

    if pil == 1:
        kechiper()

    elif pil == 2:
        keplain()

    #98 Untuk Mengakhiri Loop
    elif pil == 98:
        print(" ")
        break

    else:
        print(pil,"Tidak Ada Dalam Pilihan")