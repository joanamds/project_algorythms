import pytest
from challenges.challenge_encrypt_message import encrypt_message

# Se key e message não possuírem os tipos corretos
# uma exceção deve ser lançada


def test_encrypt_message_raises_exception_type_key():
    "Se key não tem o tipo correto deve lançar uma exceção"
    with pytest.raises(TypeError):
        encrypt_message('Message', 'key')


def test_encrypt_message_raises_exception_type_message():
    "Se message não tem o tipo correto deve lançar uma exceção"
    with pytest.raises(TypeError):
        encrypt_message(1, 1)


# Se key não for um índice positivo válido de message,
# retorna a string message invertida

def test_encrypt_message_returns_reversed_message():
    "Se key não for um positivo válido de message retorna message invertida"
    assert encrypt_message('Message', 0) == 'egasseM'
    assert encrypt_message('Message', -1) == 'egasseM'
    assert encrypt_message('Message', 7) == 'egasseM'
    assert encrypt_message('Message', 8) == 'egasseM'


# Se key for ímpar:
# divide message no índice key, inverte os caracteres de cada parte,
# e retorna a união das partes novamente com "_" entre elas
def test_encrypt_message_odd_key():
    "Se key for ímpar retorna message dividida em duas partes invertidas"
    assert encrypt_message('Message', 1) == 'M_egasse'

# Se key for par:
# divide message no índice key, inverte a posição das partes,
# inverte os caracteres de cada parte,
# e retorna a união das partes novamente com "_" entre elas


def test_encrypt_message_even_key():
    "Se key for par retorna message dividida em duas partes invertidas"
    assert encrypt_message('Message', 2) == 'egass_eM'
