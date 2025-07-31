import cv2
import numpy as np


#liga a camera
cap = cv2.VideoCapture(0)

while True:

    #ret verifica se a leitura do frame é true ou false e frame le cada frame do video
    ret, frame= cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    #desenha uma linha no diagonal na tela
    #0,0 representa w=0,h=0, canto suxperior esquerdo
    img=cv2.line(frame, (0,0), (width,height), (255,0,0), 10)

    #tem como parametro o frame, as posiçoes a ser colocado, o raio, a cor e a espessura (usar -1 qnd for preenchido)
    img=cv2.circle(img, (width//2, height//2), 100, (0,0,255), 1)

    #mostra o frame e nomeia a janela como my camera
    cv2.imshow('my camera', img)

    #a cada 1ms verifica se a tecla x foi pressionada comparando a tecla pressionada cm o ascii de x
    if cv2.waitKey(1) == ord ('x'):
        break

cap.release()
cv2.destroyAllWindows()