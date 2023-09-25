import numpy as np

# define um array vazio de inteiros
myarray = np.array([], dtype=int)

# adicionando valores
myarray = np.insert(myarray, 0, 5)  # posição 0, valor 5
myarray = np.insert(myarray, 1, 3)
myarray = np.insert(myarray, 2, 5)
print("Após adicionar alguns valores: ", myarray)

# adicionar em posição intermediária
myarray = np.insert(myarray, 1, 4)
print("Após inserção em índice intermediário: ", myarray)


# removendo
myarray = np.delete(myarray, 0)
print("Após remover um valor: ", myarray)
