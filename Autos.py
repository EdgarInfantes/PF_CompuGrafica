import cv2 as cv
from Rastreador import *

#-------------------Creamos un objeto para el seguimiento-------------------
seguimiento = Rastreador()


#-------------------Creamos una Clase que sea nuestro rastreador-------------------
cap = cv.VideoCapture("Video2.mp4")

deteccion = cv.createBackgroundSubtractorMOG2(history=10000, varThreshold=12)  # Extrae los objetos en movimiento


while True:
    ret, frame = cap.read()
    frame = cv.resize(frame, (1280, 720))  # Redimensionamos el video

    # Elegimos una zona de interés para contar el paso de autos
    #zona = frame[530:720, 300:850]
    zona = frame[:500, :500]

    # Creamos una máscara a los fotogramas con el fin de que nuestros objetos sean blancos y el fondo negro
    mascara = deteccion.apply(zona)
    _, mascara = cv.threshold(mascara, 254, 255, cv.THRESH_BINARY)  # Con este umbral eliminamos sombras
    contornos, _ = cv.findContours(mascara, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    detecciones = []  # Lista donde vamos a almacenar la info

    for contorno in contornos:
        area = cv.contourArea(contorno)
        if area > 800:
            x, y, ancho, alto = cv.boundingRect(contorno)
            cv.rectangle(zona, (x, y), (x + ancho, y + alto), (255, 255, 0), 3)
            detecciones.append([x, y, ancho, alto])
    # Rastreo de objetos
    info_id = seguimiento.rastreo(detecciones)

    for inf in info_id:
        x, y, ancho, alto, id = inf
        cv.putText(zona, str(id), (x, y - 15), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv.rectangle(zona, (x, y), (x + ancho, y + alto), (255, 255, 0), 3)

    print(info_id)
    cv.imshow("Zona de Interes", zona)
    cv.imshow("Mascara", mascara)

    key = cv.waitKey(5)

    if key == 27:
        break

cap.release()
cv.destroyAllWindows()