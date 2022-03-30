from enigma.machine import EnigmaMachine

#Memasukan Text
print(" ")
a = str(input("Input Text: "))

#Pengaturan Mesin (Dapat Diubah)
machine = EnigmaMachine.from_key_sheet(
    rotors='II IV V',
    reflector='B',
    ring_settings=[1, 20, 11],
    plugboard_settings='AV BS CG DL FU HZ IN KM OW RX'

)
#Menerjemahkan ke Chiper
machine.set_display('WXC')

msg_key = machine.process_text('KCH')

machine.set_display(msg_key)

chipertext = a
plaintext = machine.process_text(chipertext)

print(plaintext)
