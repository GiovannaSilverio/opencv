import cv2
import numpy as np


#liga a camera
cap = cv2.VideoCapture(0)

while True:

    #ret verifica se a leitura do frame é true ou false e frame le cada frame do video
    ret, frame= cap.read()


    #o metodo get retorna propriedades do video
    #3 retorna width
    width=int(cap.get(3))
    #4 retorna height
    height=int(cap.get(4))

    #preenche com zeros todos os pixels do video
    image=np.zeros(frame.shape, np.uint8)

    #diminui o tamanho da captura em 4x
    smaller_frame=cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    #colo no canto superior esquerdo de img o frame
    #:height significa da linha 0 ate a linha height/2
    image[:height//2, :width//2] = smaller_frame

    #canto inferior esquerdo
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    #canto superior direito
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)

    #canto inferior direito
    image[height//2:, width//2:] = smaller_frame


    #mostra o frame e nomeia a janela como my camera
    cv2.imshow('my camera', image)

    #a cada 1ms verifica se a tecla x foi pressionada comparando a tecla pressionada cm o ascii de x
    if cv2.waitKey(1) == ord ('x'):
        break
cap.release()
cv2.destroyAllWindows()