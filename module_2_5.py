def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

result1 = get_matrix(2, 2, 10)
for k in result1:
    print(k)

result2 = get_matrix(3, 5, 42)
for o in result2:
    print(o)

result3 = get_matrix(4, 2, 13)
for l in result3:
    print(l)