def stutends_in_instant(arrivals, departures, time_instant):
    answer = 0
    size = len(arrivals)
    for index in range(size):
        if arrivals[index] <= time_instant <= departures[index]:
            answer += 1
    return answer


# ======= outra solução, mais performatica =======


def students_in_instant2(arrivals, departures, time_instant):
    return sum(
        arrival <= time_instant <= departure
        for arrival, departure in zip(arrivals, departures)
    )


# A segunda linha usa uma expressão de compreensão para calcular o número de estudantes presentes no horário especificado. A expressão de compreensão itera sobre os horários de chegada e saída dos estudantes, retornando True se o estudante estiver presente no horário especificado e False caso contrário. A função sum() é então usada para somar todos os valores retornados pela expressão de compreensão, retornando o número total de estudantes presentes no horário especificado.
