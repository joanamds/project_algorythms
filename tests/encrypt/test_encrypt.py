import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Se key e message não possuírem os tipos corretos
    # uma exceção deve ser lançada
    with pytest.raises(TypeError):
        encrypt_message('Message', 'key')
    with pytest.raises(TypeError):
        encrypt_message(1, 1)

    # Se key não for um índice positivo válido de message,
    # retorna a string message invertida
    assert encrypt_message('Message', 0) == 'egasseM'
    assert encrypt_message('Message', -1) == 'egasseM'
    assert encrypt_message('Message', 7) == 'egasseM'
    assert encrypt_message('Message', 8) == 'egasseM'

    # Se key for ímpar
    assert encrypt_message('Message', 1) == 'M_egasse'

    # Se key for par
    assert encrypt_message('Message', 2) == 'egass_eM'
