import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Transforma a imagem de BGR para HSV
    # HSV significa Matiz (Hue), Saturação (Saturation) e Valor/Brightness (Value)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerYellow = np.array([20, 100, 100])
    upperYellow = np.array([30, 255, 255])
 
    # Cria uma máscara que mantém apenas os pixels dentro do intervalo de amarelo definido.
    # Pixels dentro do intervalo ficam com valor 255 (branco), e fora ficam 0 (preto).
    mask = cv2.inRange(hsv, lowerYellow, upperYellow)

    # Aplica a máscara na imagem original usando bitwise AND.
    # O resultado mantém somente as partes da imagem original onde a máscara é branca,
    # ou seja, só mostra as áreas amarelas detectadas, deixando o resto preto.
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('My camera', result)

    if cv2.waitKey(1) == ord('x'):
        break

cap.release()
cv2.destroyAllWindows()