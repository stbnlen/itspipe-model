import pandas as pd

def clean_dataframe(df: pd.DataFrame):
    champion_counts = df["champion"].value_counts()
    popular_champions = champion_counts[champion_counts > 4].index.tolist()
    df = df.query(
        'result != "Rehacer" and game_type != "Clash" and champion in @popular_champions'
    )

    df.loc[:, "dmg_dealt"] = df["dmg_dealt"].str.replace(",", "").astype(int)

    df.loc[:, "dmg_taken"] = df["dmg_taken"].str.replace(",", "").astype(int)

    df.loc[:, "average_tier"] = df["average_tier"].str.replace(r"\d+", "").str.strip()

    game_type_mapping = {
        "Normal": 0,
        "ARAM": 1,
        "Rango 5:5 Flex": 2,
        "Clasificatoria Solo 5vs5": 3,
        "Clash": 4,
    }
    df = df.replace({"game_type": game_type_mapping})

    champion_mapping = {
        "Zed": 0,
        "Kayn": 1,
        "Vex": 2,
        "Veigar": 3,
        "Fizz": 4,
        "LeBlanc": 5,
        "Vi": 6,
        "Sejuani": 7,
        "Sylas": 8,
        "Elise": 9,
    }
    df = df.replace({"champion": champion_mapping})
    return df