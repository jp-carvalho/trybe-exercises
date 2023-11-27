# tests/descricao_livro/test_descricao_livro.py


from src.livro.livro import Livro


def test_descricao_livro():
    livro = Livro("O Hobbit", "J.R.R. Tolkien", 310)
    assert repr(livro) == "O livro O Hobbit de J.R.R. Tolkien possui 310 páginas."
