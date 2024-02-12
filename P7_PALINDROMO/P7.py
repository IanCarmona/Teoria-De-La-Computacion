import random

import random

def construir_palindromo(longitud):
    
    if longitud <= 0:
        f.write("Regla aplicada: P -> e\n")
        return ""
    
    elif longitud == 1:
        c = random.choice(["0", "1"])
        f.write("Regla aplicada: P -> ")
        if c == "0" : 
            f.write("0\n")
        else:
            f.write("1\n")
        return c
    
    elif longitud == 2:
        c1 = random.choice(["0", "1"])
        f.write("Regla aplicada: P -> ")
        if c1 == "0" : 
            f.write("0\n")
        else:
            f.write("1\n")
        return c1 + c1
    
    else:
        palindromo = ""
        for _ in range(longitud // 2):
            caracter = random.choice(["0", "1"])
            f.write("Regla aplicada: P -> ")
            if caracter == "0":
                f.write("0P0\n")
            else:
                f.write("1P1\n")
            palindromo = caracter + palindromo + caracter
        
        if longitud % 2 == 1:
            c = random.choice(["0", "1"])
            f.write("Regla aplicada: P -> ")
            if c == "0" : 
                f.write("0\n")
            else:
                f.write("1\n")
            palindromo = palindromo[:len(palindromo) // 2] + c + palindromo[len(palindromo) // 2:]
        
        return palindromo


print('1) Manual')
print('2) Automatica')
opcion = input("Ingrese la opcion: ")

if opcion == "1":
    longitud = int(input("Ingrese la longitud del palíndromo: "))
elif opcion == "2":
    longitud = random.randint(1, 100000)
    
f = open("palindromo.txt", "w")

palindromo = construir_palindromo(longitud)

f.write("\nCadena: " + palindromo + "\n")
print("Cadena: " + palindromo + "\n")

f.close()
