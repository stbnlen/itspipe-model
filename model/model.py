import pickle
import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score

def load_data(file_path):
    try:
     df = pd.read_csv(file_path)
    except FileNotFoundError as e:
        print(f'Error: {e}')
        return None
    df = clean_dataframe(df)
    return df

def split_data(X, y, test_size=0.33, random_state=123):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test


def train_game_result_prediction_model(df):
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
    
    X = df[["kill", "death", "assist", "game_type", "tower", "cs", "dmg_taken", "dmg_dealt", "champion", "cs_per_minute"]]
    y = df["result"]

    game_result_prediction_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier())
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=123)


    game_result_prediction_pipeline.fit(X_train, y_train)

    # Guardar modelo
    with open('model.pkl', 'wb') as file:
        pickle.dump(game_result_prediction_pipeline, file)

    cross_validation_scores = cross_val_score(game_result_prediction_pipeline, X, y, cv=5)

    print(f"Cross-validation scores: {cross_validation_scores}")
    print(f"Mean score: {cross_validation_scores.mean():.4f}")


def clean_dataframe(df):
    df = df[df["result"] != "Rehacer"]
    champion_counts = df["champion"].value_counts()
    popular_champions = champion_counts[champion_counts > 4].index.tolist()
    df = df[df["champion"].isin(popular_champions)]

    df['dmg_dealt'] = df['dmg_dealt'].str.replace(',', '').astype(int)
    df['dmg_taken'] = df['dmg_taken'].str.replace(',', '').astype(int)
    df['control_wards'] = pd.to_numeric(df['control_wards'].str.replace('Control Ward', ''))
    df['cs_per_minute'] = df['cs_per_minute'].apply(lambda x: re.sub('[()]', '', x)).astype(float)

    game_type_mapping = {"Normal": 0, "ARAM": 1, "Rango 5:5 Flex": 2, "Clasificatoria Solo 5vs5": 3, "Clash": 4}
    df["game_type"] = df["game_type"].map(game_type_mapping)

    champion_mapping = {"Zed": 0, "Kayn": 1, "Vex": 2, "Veigar": 3, "Fizz": 4, "LeBlanc": 5, "Vi": 6, "Sejuani": 7, "Sylas": 8, "Elise": 9}
    df["champion"] = df["champion"].map(champion_mapping)
    return df


try:
    file_path = 'model/stats.csv'
    df = load_data(file_path)
    train_game_result_prediction_model(df)
except Exception as e:
    print(f'Error: {e}')