def count_vowels(word):  # linha 1
    vowels = "aeiou"  # linha 2
    count = 0  # linha 3
    for letter in word:  # linha 4
        if letter in vowels:  # linha 5
            count += 1  # linha 6
    return count  # linha 7


count_vowels(input("Word:"))  # linha 10
