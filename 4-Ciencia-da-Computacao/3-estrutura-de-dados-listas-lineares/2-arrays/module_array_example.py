import sys
from array import array

# define um array vazio de inteiros sem sinal
myarray = array("I")

# podemos adicionar alguns valores
myarray.insert(0, 5)  # posição 0, valor 5
myarray.insert(1, 3)
myarray.insert(2, 5)
print("Após adicionar alguns valores: ", myarray)

# adicionar em posição intermediária
myarray.insert(1, 4)
print("Após inserção em índice intermediário: ", myarray)

# remover através do índice
myarray.pop(0)
print("Após remover um valor: ", myarray)

# compara o tamanho emtre uma lista e um array
elements = list(range(100))  # definindo uma lista de 100 números
print("Tamanho da lista: ", sys.getsizeof(elements))
array_from_list = array("I", elements)  # criando um array a partir da lista
print("Tamanho do array: ", sys.getsizeof(array_from_list))
