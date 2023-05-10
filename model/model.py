from utils.load_data import load_data
from utils.train_game_result import train_game_result_prediction_model

STATS_FILE_PATH = "model/stats.csv"

try:
    df = load_data(STATS_FILE_PATH)
    train_game_result_prediction_model(df)
except Exception as e:
    print(f"Error: {e}")
