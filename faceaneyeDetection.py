import cv2

cap=cv2.VideoCapture(0)

# 1. Carregar os classificadores em cascata pré-treinados
# Certifique-se de que os arquivos .xml estão na mesma pasta do script
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# 3. Loop principal para processar cada quadro do vídeo
while True:
    # Lê um quadro da câmera
    ret, frame = cap.read()

    # 4. Converter o quadro para tons de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. Detectar rostos na imagem em tons de cinza
    # detectMultiScale retorna uma lista de retângulos (x, y, w, h) para cada rosto encontrado
    # scaleFactor: Reduz o tamanho da imagem em 1.3 a cada passo. Ajuda a encontrar rostos de vários tamanhos.
    # minNeighbors: Quantos "vizinhos" cada retângulo candidato deve ter para ser considerado um rosto. Ajuda a eliminar falsos positivos.
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # 6. Iterar sobre cada rosto detectado
    for (x, y, w, h) in faces:
        # Desenha um retângulo azul ao redor do rosto na imagem colorida original
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # 7. Criar uma "Região de Interesse" (ROI - Region of Interest)
        # Para otimizar, só vamos procurar por olhos DENTRO da área do rosto que já encontramos.
        roi_gray = gray[y:y+h, x:x+w]  # ROI em tons de cinza
        roi_color = frame[y:y+h, x:x+w] # ROI colorida (para desenhar)

        # 8. Detectar olhos dentro da ROI do rosto
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5)

        # Iterar sobre cada olho detectado
        for (ex, ey, ew, eh) in eyes:
            # Desenha um retângulo verde ao redor dos olhos
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    # 9. Mostrar o quadro resultante com as detecções
    cv2.imshow('Detector de Rosto e Olhos', frame)

    # 10. Condição de saída: Pressione 'x' para fechar a janela
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

# 11. Liberar os recursos ao final
cap.release()
cv2.destroyAllWindows()