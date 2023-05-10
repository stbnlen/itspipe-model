import os
from flask import Flask, render_template, request
from utils.make_prediction import make_prediction
from utils.get_model import model

app = Flask(__name__)

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
    prediction_text = make_prediction(inputs, model=model)
    return render_template("index.html", prediction_text=prediction_text)


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", 5000))
