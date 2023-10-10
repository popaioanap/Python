#Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"



def descompune_in_biti(numar):
    # Folosim functia bin() pentru a converti numarul in format binar
    format_binar = bin(numar)
    
    # Eliminam prefixul "0b" din reprezentarea binara
    format_binar = format_binar[2:]
    
    # Adaugam zerouri la stanga pana cand avem 8 caractere (pentru a obtine un octet)
    format_binar = format_binar.zfill(8)
    
    return format_binar

    
def num1(binar):
    # Convertim numarul in format de șir de caractere
    numar_str = str(binar)
    
    # Initializam un contor pentru cifra 1
    contor = 0
    
    # Parcurgem fiecare cifra din șirul de caractere
    for cifra in numar_str:
        if cifra == '1':
            contor += 1
    
    return contor

numar = int(input())
binar = descompune_in_biti(numar)
print(num1(binar)) 
