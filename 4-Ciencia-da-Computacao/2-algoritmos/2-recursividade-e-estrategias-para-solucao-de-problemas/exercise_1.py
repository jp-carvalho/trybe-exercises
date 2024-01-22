def conta_pares(n):
    num_pares = 0
    for num in range(n + 1):  # n+1 pq pega o próprio numero informado
        if num % 2 == 0 and num != 0:
            num_pares += 1
    return num_pares
