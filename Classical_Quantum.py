import matplotlib.pyplot as plt
from Lib_Vect_Mat_Complex import *


def final_matrix(matrix):
    """Función que halla la magnitud de una matriz de imaginarios"""
    row, column = len(matrix), len(matrix[0])
    for i in range(row):
        for j in range(column):
            matrix[i][j] = complex(abs(matrix[i][j])**2, 0)
    return matrix

def sistema_probabilistico(matrix, vectIni, clicks):
    """Función que simula un sistema probabilistico clasico"""
    if (clicks >= 0) and (type(clicks) is int):
        for x in range(clicks):
            vectIni = matrix_action_vector(matrix, vectIni)
        return vectIni
    return None

def sistema_probabilistico_quantico(matrix, vectIni, clicks):
    """Función que simula un sistema probabilistico cuantico"""
    if (clicks >= 0) and (type(clicks) is int):
        length = len(vectIni)
        copyMatrix = matrix[:]
        for x in range(clicks):
            matrix = mult_matrix(matrix, copyMatrix)
        return final_matrix(matrix)
    return -1

def canicas_booleanas(clicks, booleanMatrix, vectIni):
    """Funcion que simula experimento de canicas con coeficientes booleanos"""
    if (clicks >= 0 and type(clicks) is int):
        for c in range(clicks):
            vectIni = matrix_action_vector(booleanMatrix, vectIni)
        return vectIni


def multiple_rendija_clasico(matrix, vectIni, clicks):
    """Función que simula el experimento de multiples rendijas clasico"""
    return sistema_probabilistico(matrix, vectIni, clicks)


def multiple_rendija_cuantico(matrix, vectIni, clicks):
    """Función que simula el experimento de multiples rendijas cuantico"""
    return sistema_probabilistico_quantico(matrix, vectIni, clicks)

def grafico(vector):
    """Función que grafica un diagrama de barras que muestra las probabilidades en porcentaje de un vector de estado.
    La imagen puede guardarse en el computador."""
    data = len(vector)
    x = np.array([x for x in range(data)])
    probabilities = np.array([abs(vector[x]) ** 2 * 100 for x in range(data)])  # Calcula el módulo al cuadrado y multiplica por 100

    plt.bar(x, probabilities, color='b', align='center')

    plt.title('Probabilidades vector estado')
    plt.xlabel('Índice')
    plt.ylabel('Probabilidad (%)')
    plt.show()

