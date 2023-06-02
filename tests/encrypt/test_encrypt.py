import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Verifica se key e message não possuem os tipos corretos
    with pytest.raises(TypeError):
        encrypt_message('Message', 'key')
    with pytest.raises(TypeError):
        encrypt_message(1, 1)

    # Verifica se key não é um índice positivo válido de message
    assert encrypt_message('Message', 0) == 'egasseM'
    assert encrypt_message('Message', -1) == 'egasseM'
    assert encrypt_message('Message', 7) == 'egasseM'
    assert encrypt_message('Message', 8) == 'egasseM'

    # Verifica se key é ímpar
    assert encrypt_message('Message', 1) == 'M_egasse'

    # Verifica se key é par
    assert encrypt_message('Message', 2) == 'egass_eM'
