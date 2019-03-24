import cv2
import numpy as np

def encontrar_quadrados(erode, lado_quadrado):
    result = []
    limite = lado_quadrado-1
    for i in range(0,10):
        for j in range(0,10):
            if(erode[i,j] == 1 and len(result) == 0):
                result.append([i,j])
            elif(erode[i,j] == 1 and len(result) > 0):            
                aux = 0
                for r in result:
                    #se estiver na mesma linha verifica apenas a diferença da coluna (tamanho do quadrado - 1)
                    if(i == r[0] and abs(j-r[1]) > limite):
                            aux += 1
                    #se estiver na mesma coluna verifica apenas a diferença da linha                
                    elif(j == r[1] and abs(i-r[0]) > limite):
                            aux += 1
                    #se não esta na mesma linha nem na mesma coluna verifica apenas um ou outro
                    elif(abs(i-r[0]) > limite or abs(j-r[1]) > limite):
                            aux += 1
                if(aux == len(result)):
                    result.append([i,j])
    return result

data =  np.array([
                 [1,1,1,0,1,1,1,1,1,1],
                 [1,1,1,0,1,1,1,1,1,1],
                 [1,1,0,0,1,1,1,1,1,1],
                 [0,0,0,0,1,1,1,1,1,1],
                 [0,0,0,0,1,1,1,0,1,1],
                 [0,1,1,1,1,1,1,1,1,1],
                 [0,0,0,1,1,1,1,1,1,0],
                 [0,0,0,1,1,1,1,1,1,0],
                 [0,0,0,1,1,1,1,1,1,0],
                 [0,0,0,1,1,1,1,1,1,0],
                 ], dtype = np.uint8                 
                 )
lado_quadrado = 3

ele = cv2.getStructuringElement(cv2.MORPH_RECT,(lado_quadrado,lado_quadrado))
erode  = cv2.erode(data,ele, iterations=1,borderType=cv2.BORDER_CONSTANT,borderValue=0)

result = encontrar_quadrados(erode, lado_quadrado)

print('\nTamanho do quadrado: {}\n'.format(lado_quadrado))
print('Número de quadrados sem sobreposição encontrados: {}\n'.format(len(result)))
print('Posição central dos quadrados encontrados:\n')
print(result)

cv2.waitKey()
cv2.destroyAllWindows()