from revisao2 import search_user
from revisao2 import search_by_name
from revisao2 import add_new_user

import pytest

mock_users = [
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

mock_users_failed = [
    ("JP", "fjk2809"),
    ("Ana", 2),
    ("Tobias", "fjk2222"),
    ("Marta", "fjk9809"),
    (3232, "fjk2821"),
    ("Lais", "fjk2119"),
    ("Italo", "fjk0101"),
    ("Maria", "fjk2031"),
    ("Carol", "fjk1809"),
]

def test_search_user():
    '''
    Testa a função search_user com os parâmetros necessários e verifica se o retorno está correto
    '''
    #Verifica se a função retorna os utuários cujas senhas terminam com '1
    assert search_user(mock_users) == "Pessoas que tem a senha terminada com 1: ['Robertinho', 'Italo', 'Maria']. Total de 3 pessoas."

    # Verifica a função com uma chamada que deve levantar um TypeError
    with pytest.raises(TypeError):
        search_user(mock_users_failed)

    # Testa a função com uma chamada que deve levantar um TypeError devido a uma lista de usuários inválida
    with pytest.raises(TypeError):
        search_user()


def test_search_by_name():
    '''
    Testa a função search_by_name com os parâmetros necessários e verifica se o retorno está correto
    '''
    # Verifica se a função retorna a senha correta para o usuário fornecido
    assert search_by_name("JP", mock_users) == "A senha fjk2809 foi encontrada para o usuário: JP"

    # Testa a função cmo uma chamada que deve levantar um TypeError
    with pytest.raises(TypeError):
        search_by_name("Ana", mock_users_failed)

    #Testa a função com uma chamada que deve levantar um TypeError devido a uma lsita de usuários inválida
    with pytest.raises(TypeError):
        search_by_name()


def test_add_new_user():
    '''
    Testa a função add_new_users com os parâmetros necessários e verifica se o retorno está correto
    '''
    # Adiciona um novo usuário e verifica se foi adicionado corretamente
    add_new_user('Alberto', '159', mock_users)

    assert mock_users == [
    ("JP", "fjk2809"),
    ("Ana", "fjk2203"),
    ("Tobias", "fjk2222"),
    ("Marta", "fjk9809"),
    ("Robertinho", "fjk2821"),
    ("Lais", "fjk2119"),
    ("Italo", "fjk0101"),
    ("Maria", "fjk2031"),
    ("Carol", "fjk1809"),
    ("Alberto", '159'),
]

    # Testa a função com uma chamada que deve levantar um TypeError
    with pytest.raises(TypeError):
        add_new_user()

    # Testa a função  com uma chamada que deve levantar um TypeError devido a parâmetros inválidos
    with pytest.raises(TypeError):
        add_new_user()