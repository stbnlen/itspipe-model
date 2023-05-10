from typing import Dict, Any

MAPEO_CHAMPIONS = {
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

def make_prediction(inputs: Dict[str, Any], model) -> str:
    if not isinstance(inputs, dict):
        raise TypeError("Inputs must be a dictionary")
    if "champion" not in inputs or not isinstance(inputs["champion"], int):
        raise ValueError("Inputs must contain a 'champion' key with an integer value")
    prediction = model.predict([list(inputs.values())])
    champion = [k for k, v in MAPEO_CHAMPIONS.items() if v == inputs["champion"]][0]
    return f"La partida con {champion} es una contundente {prediction[0]}"