def count_servers(grid):
    # calcula o número de linhas e colunas da grade e armazena os resultados nas variáveis rows e columns
    rows, columns = len(grid), len(grid[0])
    # criam duas listas, servers_in_rows e servers_in_columns, que armazenarão o número de servidores em cada linha e coluna da grade
    servers_in_rows = [0 for _ in range(rows)]
    servers_in_columns = [0 for _ in range(columns)]

    #  itera sobre cada elemento da grade. Se o elemento for igual a 1, o número de servidores na linha e na coluna do elemento é incrementado em 1.
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                servers_in_rows[i] += 1
                servers_in_columns[j] += 1

    # itera sobre cada elemento da grade novamente. Se o elemento for igual a 1 e o número de servidores na linha ou na coluna do elemento for maior que 1, o valor da variável answer é incrementado em 1.
    answer = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1 and (
                servers_in_rows[i] > 1 or servers_in_columns[j] > 1
            ):
                answer += 1

    return answer
