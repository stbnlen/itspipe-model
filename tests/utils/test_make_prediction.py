import pytest
from unittest.mock import Mock
from utils.make_prediction import make_prediction

def test_make_prediction_correct_input():
    # Crea un diccionario con entradas válidas
    inputs = {
        "kill": 10,
        "death": 2,
        "assist": 5,
        "game_type": "Ranked",
        "tower": 9,
        "baron": 2,
        "dmg_dealt": 20000,
        "champion": 1
    }
    # Crea un modelo ficticio que devuelve "Victoria"
    model_mock = Mock(predict=Mock(return_value=["Victoria"]))
    # Comprueba que la función devuelve el resultado esperado
    assert make_prediction(inputs, model_mock) == "La partida con Kayn es una contundente Victoria"

def test_make_prediction_missing_champion_input():
    # Crea un diccionario sin la clave "champion"
    inputs = {
        "kill": 10,
        "death": 2,
        "assist": 5,
        "game_type": "Ranked",
        "tower": 9,
        "baron": 2,
        "dmg_dealt": 20000
    }
    # Crea un modelo ficticio que devuelve "Victoria"
    model_mock = Mock(predict=Mock(return_value=["Victoria"]))
    # Comprueba que la función lanza una excepción ValueError
    with pytest.raises(ValueError):
        make_prediction(inputs, model_mock)

def test_make_prediction_invalid_champion_input():
    # Crea un diccionario con un valor inválido para "champion"
    inputs = {
        "kill": 10,
        "death": 2,
        "assist": 5,
        "game_type": "Ranked",
        "tower": 9,
        "baron": 2,
        "dmg_dealt": 20000,
        "champion": "invalid"
    }
    # Crea un modelo ficticio que devuelve "Victoria"
    model_mock = Mock(predict=Mock(return_value=["Victoria"]))
    # Comprueba que la función lanza una excepción ValueError
    with pytest.raises(ValueError):
        make_prediction(inputs, model_mock)

