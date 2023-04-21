import pytest
import sys
sys.path.insert(0, '.')

from main import make_prediction

@pytest.fixture
def inputs():
    return {
        'kill': 10,
        'death': 2,
        'assist': 5,
        'game_type': 1,
        'tower': 5,
        'cs': 140,
        'dmg_taken': 15000,
        'dmg_dealt': 14000,
        'champion': 0,
        'cs_per_minute': 4.9
    }

def test_make_prediction(inputs):
    expected_output = 'La partida con Zed es una contundente Victoria'
    assert make_prediction(inputs) == expected_output