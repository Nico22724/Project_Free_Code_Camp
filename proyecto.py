import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz Numpy de 3 x 3
    matrix = np.array(lista).reshape(3, 3)

    # Calcular la media
    mean_axis1 = np.mean(matrix, axis=0).tolist()
    mean_axis2 = np.mean(matrix, axis=1).tolist()
    mean_flattened = np.mean(matrix).tolist()

    # Calcular la varianza
    variance_axis1 = np.var(matrix, axis=0).tolist()
    variance_axis2 = np.var(matrix, axis=1).tolist()
    variance_flattened = np.var(matrix).tolist()

    # Calcular la desviación estándar
    std_axis1 = np.std(matrix, axis=0).tolist()
    std_axis2 = np.std(matrix, axis=1).tolist()
    std_flattened = np.std(matrix).tolist()

    # Calcular el máximo
    max_axis1 = np.max(matrix, axis=0).tolist()
    max_axis2 = np.max(matrix, axis=1).tolist()
    max_flattened = np.max(matrix).tolist()

    # Calcular el mínimo
    min_axis1 = np.min(matrix, axis=0).tolist()
    min_axis2 = np.min(matrix, axis=1).tolist()
    min_flattened = np.min(matrix).tolist()

    # Calcular la suma
    sum_axis1 = np.sum(matrix, axis=0).tolist()
    sum_axis2 = np.sum(matrix, axis=1).tolist()
    sum_flattened = np.sum(matrix).tolist()

    calculations = {
        'mean': [mean_axis1, mean_axis2, mean_flattened],
        'variance': [variance_axis1, variance_axis2, variance_flattened],
        'standard deviation': [std_axis1, std_axis2, std_flattened],
        'max': [max_axis1, max_axis2, max_flattened],
        'min': [min_axis1, min_axis2, min_flattened],
        'sum': [sum_axis1, sum_axis2, sum_flattened]
    }

    return calculations

# Ejemplo de uso:
mi_lista = ([0,1,2,3,4,5,6,7,8])
matriz_resultante = calculate(mi_lista)
print(matriz_resultante)
