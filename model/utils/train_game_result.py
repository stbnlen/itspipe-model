import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

def train_game_result_prediction_model(df: pd.DataFrame) -> None:
    """
    Trains a machine learning model to predict the result of a game based on various features.

    Parameters:
    df (pandas.DataFrame): A DataFrame containing the game data.

    Returns:
    None
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a pandas DataFrame")
    if "result" not in df.columns:
        raise ValueError("DataFrame must contain a 'game_result' column")

    X = df[
        [
            "kill",
            "death",
            "assist",
            "game_type",
            "tower",
            "baron",
            "dmg_dealt",
            "champion",
        ]
    ].copy()

    X.columns = [
        "kill",
        "death",
        "assist",
        "game_type",
        "tower",
        "baron",
        "dmg_dealt",
        "champion",
    ]

    y = df["result"]

    game_result_prediction_pipeline = Pipeline(
        [("scaler", StandardScaler()), ("classifier", AdaBoostClassifier())]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=123
    )

    game_result_prediction_pipeline.fit(X_train, y_train)

    # Guardar modelo
    with open("model.pkl", "wb") as file:
        pickle.dump(game_result_prediction_pipeline, file)

    cross_validation_scores = cross_val_score(
        game_result_prediction_pipeline, X, y, cv=5
    )

    print(f"Cross-validation scores: {cross_validation_scores}")
    print(f"Mean score: {cross_validation_scores.mean():.4f}")