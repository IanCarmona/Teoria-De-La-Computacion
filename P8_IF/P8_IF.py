import random


def generar_codigo(texto_final):
    def sangrias(espacios):
        return "   " * espacios

    espacios = 0
    
    with open("pseudocodigo.txt", "a", encoding="utf-8") as archivo:
        for caracter in texto_final:
            if caracter == "(":
                espacios += 1
                
            elif caracter == ")":
                espacios -= 1

            if caracter == 'i':
                cadena_espacios = sangrias(espacios)
                archivo.write(f"\n{cadena_espacios}if ")
            elif caracter == 'C':
                archivo.write("(CONDICIONAL)")
            elif caracter == 't':
                archivo.write(":")
            elif caracter == 'S':
                cadena_espacios = sangrias(espacios + 1)
                archivo.write(f"\n{cadena_espacios}CODIGO")
            elif caracter == 'e':
                cadena_espacios = sangrias(espacios)
                archivo.write(f"\n{cadena_espacios}else")

def procesar_if(n):
    def quitar_a(texto_con_a):
        def elegir_cadena():
            return "eS" if random.randint(0, 1) == 0 else ""

        ubicaciones = [i for i, c in enumerate(texto_con_a) if c == "A"]
        if not ubicaciones:
            return texto_con_a

        nueva_cadena = texto_con_a  # Copiamos la cadena base para modificarla

        with open("derivaciones.txt", 'a', encoding='utf-8') as archivo:
            archivo.write(f"S -> {texto_con_a}\n")
            for i in ubicaciones:
                eleccion_a = elegir_cadena()
                nueva_cadena = nueva_cadena[:i] + eleccion_a + nueva_cadena[i + 1:]
                archivo.write(f"{eleccion_a} -> {nueva_cadena}\n")
        return nueva_cadena


    def concatenar_texto(texto):
        ubicaciones = [i for i, c in enumerate(texto) if c == "S"]
        if not ubicaciones:
            return texto

        opciones = random.randint(0, len(ubicaciones) - 1)
        posicion = ubicaciones[opciones]

        nuevo_texto = texto[:posicion] + "(iCtSA)" + texto[posicion + 1:]
        nuevo_texto = quitar_a(nuevo_texto)
        return nuevo_texto

    construyendo = "iCtSA"
    if n == 1:
        quitar_a(construyendo)
    else:
        for _ in range(n - 1):
            construyendo = concatenar_texto(construyendo)

    generar_codigo(construyendo)

while True:
    
    
    
    print("1) Manual")
    print("2) Automático")
    print("3) Salir")
    opcion = int(input("Ingrese su opción: "))
    
    with open("derivaciones.txt", 'w', encoding='utf-8') as w:
        w.write("")

    with open("pseudocodigo.txt", "w", encoding="utf-8") as w:
        w.write("")
        
    if opcion == 1:
        num_ifs = int(input("\nNúmero de ifs: "))
        if 0 < num_ifs < 1000:
            procesar_if(num_ifs)
            
    elif opcion == 2:
        num_ifs = random.randint(0, 1000)
        procesar_if(num_ifs)
        
    elif opcion == 3:
        break
    
    else:
        print("Opción incorrecta.")
