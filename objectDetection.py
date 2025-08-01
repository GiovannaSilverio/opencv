import cv2
import numpy as np

# A imagem principal onde vamos procurar
img_principal = cv2.imread('assets/futebol.png', 0)

#copia
img_para_desenhar = img_principal.copy()

# O template para a busca no caso a bola
template = cv2.imread('assets/bola.png',0)


# Extrai a largura e altura do template. 
h, w = template.shape

# A função matchTemplate desliza o template sobre a imagem principal e gera o mapa de calor
# TM_CCOEFF_NORMED é um dos melhores métodos de comparação.
# Valores mais altos significam melhor correspondência.
resultado = cv2.matchTemplate(img_principal, template, cv2.TM_CCOEFF_NORMED)

# Encontrar a melhor correspondência no mapa de calor
# cv2.minMaxLoc nos dá o valor mínimo, máximo e suas localizações no mapa de resultado
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

# Como usamos TM_CCOEFF_NORMED, o melhor resultado está no valor máximo (max_val) e na sua localização (max_loc)
# max_loc nos dará a coordenada do canto superior esquerdo da melhor correspondência
ponto_superior_esquerdo = max_loc
ponto_inferior_direito = (ponto_superior_esquerdo[0] + w, ponto_superior_esquerdo[1] + h)

# Definir um "limiar de confiança". Se a melhor correspondência for muito baixa, provavelmente não é uma bola de verdade.
limiar_confianca = 0.8 

if max_val >= limiar_confianca:
    print(f"Bola encontrada com {max_val*100:.2f}% de confiança.")
    # Desenhar um retângulo ao redor do objeto encontrado
    cv2.rectangle(img_para_desenhar, ponto_superior_esquerdo, ponto_inferior_direito, (0, 255, 0), 2)
    


cv2.imshow('Resultado', img_para_desenhar)

cv2.waitKey(0)
cv2.destroyAllWindows()