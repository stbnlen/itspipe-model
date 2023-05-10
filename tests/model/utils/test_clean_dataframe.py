import pandas as pd
import pytest
from model.utils.clean_dataframe import clean_dataframe

@pytest.fixture
def example_dataframe():
    data = {
        "game_type": ["Normal", "Normal", "Clash", "Rango 5:5 Flex", "ARAM", "Clasificatoria Solo 5vs5"],
        "result": ["Victoria", "Derrota", "Victoria", "Victoria", "Derrota", "Victoria"],
        "champion": ["Zed", "Kayn", "Vex", "Veigar", "Fizz", "LeBlanc"],
        "dmg_dealt": ["10,000", "20,000", "30,000", "40,000", "50,000", "60,000"],
        "dmg_taken": ["1,000", "2,000", "3,000", "4,000", "5,000", "6,000"],
        "average_tier": ["Platinum 4", "Diamond 2", "Gold 3", "Silver 1", "Bronze 4", "Challenger"],
    }
    return pd.DataFrame(data)

def test_clean_dataframe_removes_unwanted_rows(example_dataframe):
    cleaned_df = clean_dataframe(example_dataframe)
    assert "Clash" not in cleaned_df["game_type"].values
    assert "Rehacer" not in cleaned_df["result"].values
    assert all(champ in [0, 1, 2, 3, 4, 5] for champ in cleaned_df["champion"].unique())

def test_clean_dataframe_does_not_modify_original_dataframe(example_dataframe):
    original_shape = example_dataframe.shape
    _ = clean_dataframe(example_dataframe)
    assert example_dataframe.shape == original_shape
    assert example_dataframe.equals(example_dataframe)

def test_clean_dataframe_replaces_categorical_values(example_dataframe):
    cleaned_df = clean_dataframe(example_dataframe)
    assert all(
        game_type in [0, 1, 2, 3, 4]
        for game_type in cleaned_df["game_type"].unique()
    )
    assert all(
        champ in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for champ in cleaned_df["champion"].unique()
    )