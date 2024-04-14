def transponed_matrix(matrix1):
    """Функция для транспонирования матрицы."""
    rows = len(matrix1)
    columns = len(matrix1[0])
    trans_matrix = [[0 for _ in range(rows)] for _ in range(columns)]
    for i in range(rows):
        for j in range(columns):
            trans_matrix[i][j] = matrix1[j][i]
    return(trans_matrix)


if __name__ in '__main__':
    start_matrix = [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
                ]
    print(transponed_matrix(start_matrix))
