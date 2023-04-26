import os
from flask import Flask, render_template, request
from typing import Dict, Any
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

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


def make_prediction(inputs: Dict[str, Any]) -> str:
    if not isinstance(inputs, dict):
        raise TypeError("Inputs must be a dictionary")
    if "champion" not in inputs or not isinstance(inputs["champion"], int):
        raise ValueError("Inputs must contain a 'champion' key with an integer value")
    prediction = model.predict([list(inputs.values())])
    champion = [k for k, v in MAPEO_CHAMPIONS.items() if v == inputs["champion"]][0]
    return f"La partida con {champion} es una contundente {prediction[0]}"


@app.route("/")
def index():
    """
    Renders the index.html template.

    Returns:
    The rendered HTML template.
    """
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    INPUT_KEYS = [
        "kill",
        "death",
        "assist",
        "game_type",
        "tower",
        "baron",
        "dmg_dealt",
        "champion",
    ]
    inputs = {key: int(request.form[key]) for key in INPUT_KEYS}
    prediction_text = make_prediction(inputs)
    return render_template("index.html", prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", 5000))
