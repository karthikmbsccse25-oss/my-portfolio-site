def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for i in range(cols):
        row = []
        for j in range(rows):
            row.append(matrix[j][i])
        result.append(row)

    return result


matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(matrix))