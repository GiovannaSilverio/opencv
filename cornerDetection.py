import cv2
import numpy as np

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)

# converte a imagem para escala de cinza
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecta até 100 cantos na imagem com qualidade mínima de 0.01 e distância mínima de 10 entre eles
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)

# converte os pontos detectados para inteiros (formato necessário para desenhar os círculos)
corners = np.int0(corners)

# para cada canto detectado, desenha um círculo azul na imagem original
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
