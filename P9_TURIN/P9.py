import random
import pygame
import re
import sys

def graficarMaquina():
    pygame.init()

    width, height = 600, 200
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("MAQUINA DE TURING")

    font = pygame.font.Font(None, 30)

    f = open('./resultados.txt', 'r')
    text = f.read()

    matchesCinta = re.findall(r'\[(.*?)\]', text)
    matchesRegla = re.findall(r'\((.*?)\)', text)
    matchesEstado = re.findall(r'q[0-9]+', text)

    running = True
    i = 0
    
    while running:
        
        screen.fill((0, 0, 0))

        if i < len(matchesCinta):
            matchCinta = matchesCinta[i]
            matchEstado = matchesEstado[i]
            matchRegla = matchesRegla[i]

            pygame.draw.rect(screen, (0, 0, 255), (50, 150, 500, 40))
            pygame.draw.rect(screen, (0, 255, 0), (50, 100, 90, 40))
            pygame.draw.rect(screen, (255, 0, 0), (280, 45, 100, 40)) 
            
            estado_text = font.render(matchEstado, True, (255, 255, 255))
            cinta_text = font.render(matchCinta, True, (255, 255, 255))
            regla_text = font.render(matchRegla, True, (255, 255, 255))

            screen.blit(estado_text, (70, 120))  
            screen.blit(cinta_text, (70, 160))
            screen.blit(regla_text, (300, 45))
            
            i += 1
            pygame.display.flip()
            pygame.time.wait(500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

def maquina_turing(cinta):
    
    f = open('resultados.txt', 'w')
    
    cinta = list(cinta)
    
    estado = 'q0'
    index = 0
    
    f.write(f"({str(estado)}, X, R): {str(cinta)}\n")
    
    while estado != "qf":
        if estado == 'q0':
            if index >= len(cinta):
                return False
            
            if cinta[index] == '0':
                cinta[index] = 'X'
                index += 1
                estado = 'q1'
                
                f.write(f"({str(estado)}, X, R): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index += 1
                estado = 'q3'
                
                f.write(f"({str(estado)}, Y, R): {str(cinta)}\n")
                
            else:
                return False
        elif estado == 'q1':
            
            if index >= len(cinta):
                return False
            
            if cinta[index] == '0':
                cinta[index] = '0'
                index += 1
                
                f.write(f"({str(estado)}, 0, R): {str(cinta)}\n")
                
            elif cinta[index] == '1':
                cinta[index] = 'Y'
                index -= 1
                estado = 'q2'
                
                f.write(f"({str(estado)}, Y, L): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index += 1
                
                f.write(f"({str(estado)}, Y, R): {str(cinta)}\n")
            else:
                return False
        elif estado == 'q2':
            
            if index >= len(cinta):
                return False
            
            if cinta[index] == '0':
                cinta[index] = '0'
                index -= 1
                
                f.write(f"({str(estado)}, 0, L): {str(cinta)}\n")
            elif cinta[index] == 'X':
                cinta[index] = 'X'
                index += 1
                estado = 'q0'
                
                f.write(f"({str(estado)}, X, R): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index -= 1
                
                f.write(f"({str(estado)}, Y, L): {str(cinta)}\n")
            else:
                return False
        elif estado == 'q3':
            if index >= len(cinta):
                estado = 'qf'
                
                f.write(f"({str(estado)}, B, R): {str(cinta)}\n")
                
            elif cinta[index] == 'Y':
                cinta[index] = 'Y'
                index += 1
                
                f.write(f"({str(estado)}, Y, R): {str(cinta)}\n")
            else:
                return False
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

esValida = maquina_turing(entrada)
        
if esValida:
    print("Cadena aceptada")
else:
    print("No es valida")
    
if len(entrada) <= 16:
    graficarMaquina()
