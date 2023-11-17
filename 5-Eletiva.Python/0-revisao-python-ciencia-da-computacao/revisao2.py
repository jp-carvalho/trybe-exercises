# Inicie um ambiente virtual
users = [
    ("JP", "fjk2809"),
    ("Ana", "fjk2203"),
    ("Tobias", "fjk2222"),
    ("Marta", "fjk9809"),
    ("Robertinho", "fjk2821"),
    ("Lais", "fjk2119"),
    ("Italo", "fjk0101"),
    ("Maria", "fjk2031"),
    ("Carol", "fjk1809"),
]

# Todas as pessoas cadastradas no sistema da empresa

# 1- Crie uma funcionalidade que encontre todos os usuários que o ultimo digito da senha é 1 e retorne o nome da pessoa em uma lista. Faça também a contagem de quantas pessoas são com esse final de senha

# usando endswith()
def search_user(list_users):
    if not list_users:
        raise TypeError

    result = list()
    for name, password in list_users:
        # Verifica se é sempre uma string informada
        if not isinstance(name, str) or not isinstance(password, str):
            raise TypeError
        if password.endswith('1'):
            result.append(name)
    return f"Pessoas que tem a senha terminada com 1: {result}. Total de {len(result)} pessoas."

print(search_user(users))



# 2 - Crie uma função que busque a senha do usuário pelo nome retornando a string: A senha {password} foi encontrada para o usuário: {name}
def search_by_name(name_user, list_users):
    if not list_users:
        raise TypeError
    for name, password in list_users:
        if not isinstance(name, str) or not isinstance(password, str):
            raise TypeError
        if name == name_user:
            return f"A senha {password} foi encontrada para o usuário: {name}"
        
print(search_by_name("Lais", users))



# 3 - Implemente uma função que receba nome, senha e adicione na lista de usuários

def add_new_user(name, password, list_users):
    if not name or not password or not list_users:
        raise TypeError
    tupla = (name, password)
    list_users.append(tupla)

add_new_user('Roberval', '123456', users)
print(users)

