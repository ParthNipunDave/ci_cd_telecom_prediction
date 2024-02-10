import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def test():
    dics = pickle.load(open("encoding.pkl", "rb"))

    return render_template("test.html", results=dics)


@app.route("/predict", methods=["GET"])
def predict():
    if request.method == "GET":
        tenure = request.args.get("tenure")
        security = request.args.get("security")
        tech = request.args.get("tech")
        contract = request.args.get("contract")
        charges = request.args.get("charges")
    model = pickle.load(open("randomforest.sav", "rb"))
    input_data = [[tenure, security, tech, contract, charges]]
    prediction = model.predict(input_data)[0]
    print(prediction)
    answers = {"0": "Not Churn", "1": "Churn"}
    prediction = answers[str(prediction)]
    return render_template("output.html", results=prediction)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
