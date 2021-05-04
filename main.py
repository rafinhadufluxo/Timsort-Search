# Python3 program to perform basic timSort
MIN_MERGE = 32 #O tamanho da execução pode variar de 32 a 64, dependendo do tamanho da matriz
 
def calcMinRun(n):
    """Retorna o comprimento mínimo de um
    correr de 23-64 para que
    o len (array) / minrun é menor que ou
    igual a uma potência de 2.
 
    e.g. 1=>1, ..., 63=>63, 64=>32, 65=>33,
    ..., 127=>64, 128=>32, ...
    """
    r = 0
    while n >= MIN_MERGE:
        r |= n & 1
        n >>= 1
    return n + r
 
 
# Esta função classifica a matriz do índice esquerdo para
# para o índice da direita que é de tamanho no máximo RUN
def insertionSort(arr, left, right):
    for i in range(left + 1, right + 1):
        j = i
        while j > left and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
 
 
# A função de mesclagem mescla as execuções classificadas
def merge(arr, l, m, r):
     
    # a matriz original está quebrada em duas partes
    # matriz esquerda e direita

    len1, len2 = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len1):
        left.append(arr[l + i])
    for i in range(0, len2):
        right.append(arr[m + 1 + i])
 
    i, j, k = 0, 0, l
     
    # depois de comparar, nós mesclamos essas duas matrizes
    # em uma submatriz maior
    while i < len1 and j < len2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
 
        else:
            arr[k] = right[j]
            j += 1
 
        k += 1
 
    # Copie os elementos restantes da esquerda, se houver

    while i < len1:
        arr[k] = left[i]
        k += 1
        i += 1
 
    # Copie o elemento restante do direito, se houver

    while j < len2:
        arr[k] = right[j]
        k += 1
        j += 1
 
 
# Função Timsort iterativa para classificar o
# array[0...n-1] (similar to merge sort)
def timSort(arr):
    n = len(arr)
    minRun = calcMinRun(n)


    # classificar submatrizes individuais de tamanho RUN
    for start in range(0, n, minRun):
        end = min(start + minRun - 1, n - 1)
        
        insertionSort(arr, start, end)
        
    # Comece a mesclar a partir do tamanho RUN (ou 32
    # para formar o tamanho 64, então 128, 256 e assim por diante ....
    size = minRun
    while size < n:
         
        # Escolha o ponto de partida do subarray esquerdo. Nós
        # vao se merge arr[left..left+size-1]
        # and arr[left+size, left+2*size-1]
        # Após cada fusão, aumentamos o tamanho para a esquerda em 2 *

        for left in range(0, n, 2 * size):
 
            # Encontre o ponto final da submatriz esquerda
            # mid + 1 é o ponto inicial da submatriz direita
            mid = min(n - 1, left + size - 1)
            right = min((left + 2 * size - 1), (n - 1))
 
            # Merge sub array arr[left.....mid] &
            # arr[mid+1....right]
            if mid < right:
                merge(arr, left, mid, right)
 
        size = 2 * size
 
 
# Começando o programa!
if __name__ == "__main__":
 
    arr = [-2, 7, 15, -14, 0, 15, 0,
           7, -7, -4, -13, 5, 8, -14, 12] 
 
    print("Given Array is")
    print(arr)
 
    # chamando função TimSort
    timSort(arr)
 
   # print("After Sorting Array is")
    #print(arr)
    # [-14, -14, -13, -7, -4, -2, 0, 0,
    #       5, 7, 7, 8, 12, 15, 15]