import random
import time
from tkinter import Canvas, Tk

class Pila:
    def __init__(self):
        self.items = []
    
    def estaVacia(self):
        return self.items == ['Z0']
    
    def empujar(self, item):
        self.items.append(item)
    
    def sacar(self):
        return self.items.pop()
    
    def verTope(self):
        return self.items[len(self.items)-1]
    
    def tamano(self):
        return len(self.items)
    
def automataPila(pila: Pila, entrada):
    equis = "X"
    bandera = True
    for i in range(len(entrada)):
        bit = entrada[i]
        
        if bit == "0":
            if i == 0:
                f.write(f"d(q, 0, Z0) = [(q, {equis}Z0)]")
            else:
                equis += 'X'
                f.write(f"d(q, 0, X) = [(q, {equis}Z0)]")
                
            pila.empujar('X')
        else:
            if bandera == True:
                f.write(f"d(q, 1, {equis}) = [(p, {equis[:-1]})]\n")
                bandera = False
            
            if equis[:-1] != '':
                f.write(f"d(p, 1, {equis}) = [(p, {equis[:-1]})]")
            else:
                f.write(f"d(p, 1, {equis}) = [(p, e)]")
                
            equis = equis[:-1]
                
            if pila.estaVacia():
                return False

            pila.sacar()
            
        f.write("\n")
    
    if pila.verTope() != 'Z0':
        return False
    
    return True
    
def automataPila_Grafica(pila, entrada):
    i = 0
    aux = entrada
    
    canv.create_rectangle(300, 150, 350, 200, width=0, fill='red')
    canv.create_line(325, 150, 325, 100, arrow="last")
    canv.create_line(325, 200, 325, 250, arrow="last")
    canv.create_text(325, 75, text=entrada, tags="entrada1")
    canv.create_text(325, 275, text="Z0", tags="pila{i}")
    canv.pack()
    
    x = 325 
    y = 325
    x2 = 325
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
            pila.empujar('X')
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
            if (pila.estaVacia()):
                return False
            i -= 1
            canv.delete(f"pila{i}")
            pila.sacar()
            
        canv.delete("entrada")
        aux = entrada[j + 1:]
        canv.create_text(x2, y2, text=str(aux), tags="entrada")
        canv.update()
        
        time.sleep(3)
        f.write("\n")
            
    canv.update() 
    if pila.verTope() != 'Z0': 
        return False
    
    f.write("d(p, e, Z0) = [(f, Z0)]")
    return True
    

# Creamos un menu para elejir el modo
print("Elija el modo:")
print("1. Automatico")
print("2. Manual")
opc = input("Inserte su opcion deseada: ")
entrada = ""

# Creamos una cadena aleatoria o le pedimos al usuario su cadena
if opc == '1':
    cantidadCeros = random.randint(1, 50)
    cantidadUnos = random.randint(1, 50)
    print("Cantidad ceros: ", cantidadCeros)
    print("Cantidad unos: ", cantidadUnos)
    
    for i in range(cantidadCeros):
        entrada += '0'
    for i in range(cantidadUnos):
        entrada += '1'
else:
    entrada = input("Inserte su cadena: ")

# Mostramos la cadena creada
print("Su entrada fue: ", entrada)

# Inicializamos la pila
pila = Pila()
pila.empujar('Z0')

# Abrimos el archuivo de texto donde guardamos los estados
f = open("evaluacionPila.txt", 'w')

# Evaluamos la cadena en el automata
# Si la cadena es menor que 10, animamos la pila, en otro caso no
esValida = False
if len(entrada) < 10:
    #Creamos la ventana para la animacion
    ventana = Tk()
    canv = Canvas(ventana, width=800, height=800)
    ventana.geometry("600x600")
    esValida = automataPila_Grafica(pila, entrada)
    canv.update()
    canv.place(x=0, y=0)
    ventana.mainloop()
else:
    esValida = automataPila(pila, entrada)
 
# Verificamos los resultados         
if esValida:
    print("Tope: ", pila.verTope())
    print("Cadena aceptada")
else:
    print("Tope: ", pila.verTope())
    print("No es valida")