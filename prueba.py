import cv2 as cv

# Ruta del video
video_path = 'Video.mp4'

# Cargar el video
cap = cv.VideoCapture(video_path)

# Obtener las dimensiones del video
video_width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
video_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Crear una ventana con el tamaño del video
cv.namedWindow("Video con ROI", cv.WINDOW_NORMAL)
cv.resizeWindow("Video con ROI", video_width, video_height)

# Definir la región de interés (ROI)
x, y, width, height = 500, 500, 500, 500  # Región de interés en cuadro

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Dibujar un rectángulo rojo en la región de interés
    cv.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)

    # Mostrar el fotograma con la región de interés marcada
    cv.imshow("Video con ROI", frame)

    # Esperar 25 ms entre fotogramas (ajustar para controlar la velocidad)
    if cv.waitKey(25) & 0xFF == ord('q'):
        break

# Liberar el objeto de captura y cerrar las ventanas
cap.release()
cv.destroyAllWindows()
