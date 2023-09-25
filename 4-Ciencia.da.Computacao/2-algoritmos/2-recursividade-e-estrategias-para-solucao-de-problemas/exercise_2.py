def conta_pares(n):
    # condição de parada
    if n == 1:
        return 0

    # Caso seja par, soma 1 e volta ao início
    elif n % 2 == 0:
        return 1 + conta_pares(n - 1)

    # Caso seja ímpar - volta ao início
    else:
        return conta_pares(n - 1)
