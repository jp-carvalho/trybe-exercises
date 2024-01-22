# EXERCÍCIO 01


# Encontre o número mais frequente, se houver empate, retorne qualquer um.abs
# nums = [3, 2, 5, 4, 1, 2, 3, 1, 3, 4, 1]
def count(nums):
    count = {}
    most_frequent = nums[0]

    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

        if count[num] > count[most_frequent]:
            most_frequent = num

    return most_frequent


# EXERCÍCIO 02
# Separe as palavras de acordo com sua letra inicial
# text = ['Ana', 'ama', 'Joao', 'que', 'ama', 'Jose', 'mais', 'Jose', 'nao', 'ama', 'Ana']
# respostas:
# a: ['Ana', 'ama', 'ama', 'ama', 'Ana']
# b: ['Joao', 'Jose', 'Jose"]
# c: ['que']
# d: ['mas']
# e: ['nao']


def screening(text):
    screen = {}

    for word in text:
        first_char = word[0]
        if first_char not in screen:
            screen[first_char] = [word]
        else:
            screen[first_char].append(word)
    return screen


# EXERCÍCIO 03
# Quais elementos da lista A ocorrem na lista B?
# listA = [1, 2, 3, 4, 5, 6]
# listB = [4, 5, 6, 7, 8, 9]
# resposta [4, 5, 6]


def intersection(listA, listB):
    seen_in_a = {}

    for item in listA:
        if item not in seen_in_a:
            seen_in_a[item] = True

    ans = []
    for item in listB:
        if item in seen_in_a:
            ans.append(item)

    return ans
