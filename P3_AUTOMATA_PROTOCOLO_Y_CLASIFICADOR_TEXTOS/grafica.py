import cv2
import numpy as np

# Crear una imagen en blanco
width, height = 1000, 600
image = np.zeros((height, width, 3), dtype=np.uint8)

# Definir el centro y el radio del círculo
circle_center = (220, 300)
circle_radius = 200

# Definir la fuente y otros parámetros de texto
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1.5
font_color = (0, 0, 0)  # Color del texto en formato BGR
font_thickness = 2



# Dibujar el círculo en la imagen
cv2.circle(image, circle_center, circle_radius, (255, 0, 0), thickness=2)
cv2.circle(image, circle_center, 150, (255, 0, 0), thickness=2)
cv2.circle(image, (220, 125), 40, (0, 255, 0), thickness=cv2.FILLED)
cv2.circle(image, (220, 125), 30, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (220, 125), 40, (255, 255, 255), thickness=2)
cv2.circle(image, (395, 300), 40, (0, 0, 255), thickness=cv2.FILLED)
#cv2.circle(image, (675, 300), 30, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (220, 470), 40, (0, 0, 255), thickness=cv2.FILLED)
#cv2.circle(image, (500, 470), 30, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (45, 300), 40, (0, 0, 255), thickness=cv2.FILLED)
#cv2.circle(image, (325, 300), 30, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (254, 154), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (414, 256), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (178, 103), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (73, 264), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (259, 494), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (26, 344), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (190, 444), 5, (255, 255, 255), thickness=cv2.FILLED)
cv2.circle(image, (373, 338), 5, (255, 255, 255), thickness=cv2.FILLED)


# Agregar el texto a la imagen
cv2.putText(image, "E1", (195, 140) , font, font_scale, font_color, font_thickness)
cv2.putText(image, "E2", (370, 315) , font, font_scale, font_color, font_thickness)
cv2.putText(image, "E3", (195, 485) , font, font_scale, font_color, font_thickness)
cv2.putText(image, "E4", (20, 315) , font, font_scale, font_color, font_thickness)

cv2.putText(image, "0", (370, 144) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "0", (273, 255) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "1", (373, 470) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "1", (273, 383) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "0", (113, 381) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "0", (40, 477) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "1", (109, 244) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "1", (40, 145) , font, font_scale, (255, 255, 255), font_thickness)
cv2.putText(image, "START", (80, 80) , font, 0.5, (0, 255, 0), font_thickness)
cv2.putText(image, "START", (750, 55) , font, 0.5, (0, 255, 0), font_thickness)



# Definir puntos para dibujar la flecha
arrow_start = (0, 85)
arrow_end = (220, 85)

# Dibujar la flecha en la imagen
cv2.arrowedLine(image, arrow_start, arrow_end, (0, 255, 0), thickness=2, tipLength=0.1)
cv2.arrowedLine(image,(740,150) , (740, 330), (0, 255, 0), thickness=2, tipLength=0.1)
cv2.arrowedLine(image,(670, 400) , (450, 400), (0, 255, 0), thickness=2, tipLength=0.1)
cv2.arrowedLine(image,(450, 150) , (670, 150), (0, 255, 0), thickness=2, tipLength=0.1)
cv2.arrowedLine(image,(740,0) , (740,70), (0, 255, 0), thickness=2, tipLength=0.1)


cv2.rectangle(image, (5, 47), (445, 520), (255, 255, 255), thickness=2)
cv2.rectangle(image, (740, 400), (850, 520), (0, 255, 0), thickness=2)
cv2.circle(image, (740, 480), 5, (0, 255, 0), thickness=cv2.FILLED)

cv2.circle(image, (740, 150), 70, (255, 0, 255), thickness=cv2.FILLED)
cv2.circle(image, (740, 400), 70, (255, 0, 255), thickness=cv2.FILLED)

cv2.putText(image, "READY", (700, 150) , font, .8, (255, 255, 255), font_thickness)
cv2.putText(image, "SENDING", (690, 400) , font, .8, (255, 255, 255), font_thickness)
cv2.putText(image, "DATA IN", (750, 270) , font, .5, (255, 255, 255), font_thickness)
cv2.putText(image, "TIME-OUT", (860, 470) , font, .5, (255, 255, 255), font_thickness)


# Mostrar la imagen resultante
cv2.imshow("Círculo con Flecha", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
