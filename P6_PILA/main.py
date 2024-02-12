import random
import time
from tkinter import Canvas, Tk

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == ['Z0']

    def apilar(self, elemento):
        self.items = self.items + [elemento]

    def desapilar(self):
        
        self.items = self.items[:-1]  
        return self.items

    def ver_tope(self):
        return self.items[len(self.items)-1]

    def tamano(self):
        return len(self.items)


def esta_valida(pila: Pila, cadena):
    
    x = "X"
    bandera = True
    
    for i in range(len(cadena)):
        bit = cadena[i]
        
        if bit == "0":
            if i == 0:
                f.write(f"(q, 0, Z0) = [(q, {x}Z0)]")
            else:
                x += 'X'
                f.write(f"(q, 0, X) = [(q, {x}Z0)]")
                
            pila.apilar('X')
        else:
            if bandera == True:
                f.write(f"(q, 1, {x}) = [(p, {x[:-1]})]\n")
                bandera = False
            
            if x[:-1] != '':
                f.write(f"(p, 1, {x}) = [(p, {x[:-1]})]")
            else:
                f.write(f"(p, 1, {x}) = [(p, e)]")
                
            x = x[:-1]
                
            if pila.esta_vacia():
                return False

            pila.desapilar()
            
        f.write("\n")
        
    
    if pila.ver_tope() != 'Z0':
        return False
    
    return True
    

def automataPila_Grafica(pila, entrada):
    i = 0
    aux = entrada
    
    canv.create_rectangle(200, 150, 250, 200, width=0, fill='yellow')
    canv.create_line(225, 150, 225, 100, arrow="last")
    canv.create_line(225, 200, 225, 250, arrow="last")
    canv.create_text(225, 175, text=entrada, tags="entrada1")
    canv.create_text(225, 275, text="Z0", tags="pila{i}")
    canv.pack()
    
    x = 225 
    y = 225
    x2 = 225
    y2 = 75

    canv.update()
    time.sleep(2)
    
    equis = "X"
    bandera = True
    for j in range(len(entrada)):
        bit = entrada[j]
        f.write(aux + "\n")   
        canv.delete("entrada1")
                
        if bit == '0':
            if j == 0:
                f.write(f"d(q, 0, Z0) = [(q, {equis}Z0)]")
            else:
                equis += 'X'
                f.write(f"d(q, 0, X) = [(q, {equis}Z0)]")
            canv.create_text(x, y, text="X", tags=f"pila{i}")
            pila.apilar('X')
            i += 1
            y += 50
            
        else: 
            if bandera == True:
                f.write(f"d(q, 1, {equis}) = [(p, {equis[:-1]})]\n")
                bandera = False
            
            if equis[:-1] != '':
                f.write(f"d(p, 1, {equis}) = [(p, {equis[:-1]})]")
            else:
                f.write(f"d(p, 1, {equis}) = [(p, e)]")
            
            equis = equis[:-1]
                
            y -= 50
            if (pila.esta_vacia()):
                return False
            i -= 1
            canv.delete(f"pila{i}")
            pila.desapilar()
            
        canv.delete("entrada")
        aux = entrada[j + 1:]
        canv.create_text(x2, y2, text=str(aux), tags="entrada")
        canv.update()
        
        time.sleep(1)
        f.write("\n")
            
    canv.update() 
    if pila.ver_tope() != 'Z0': 
        return False
    
    f.write("d(p, e, Z0) = [(f, Z0)]")
    return True
    

print("Elija el modo:")
print("1. Automatico")
print("2. Manual")
opc = input("Inserte su opcion deseada: ")
entrada = ""

if opc == '1':
    cantidadCeros = random.randint(1, 500)
    cantidadUnos = random.randint(1, 500)
    print("Cantidad ceros: ", cantidadCeros)
    print("Cantidad unos: ", cantidadUnos)
    
    for i in range(cantidadCeros):
        entrada += '0'
    for i in range(cantidadUnos):
        entrada += '1'
else:
    entrada = input("Inserte su cadena: ")

print("Su entrada fue: ", entrada)

pila = Pila()
pila.apilar('Z0')

f = open("Pila.txt", 'w')

esValida = False
if len(entrada) <= 10:
    ventana = Tk()
    canv = Canvas(ventana, width=500, height=500)
    ventana.geometry("500x500")
    esValida = automataPila_Grafica(pila, entrada)
    canv.update()
    canv.place(x=0, y=0)
    ventana.mainloop()
else:
    esValida = esta_valida(pila, entrada)
    
if esValida:
    print("Tope: ", pila.ver_tope())
    print("Cadena aceptada")
else:
    print("Tope: ", pila.ver_tope())
    print("No es valida")
