from flask import Flask, request, jsonify
from recommendation_engine import recommend

app = Flask(__name__)

@app.route("/recommend", methods=["POST"])
def get_recommendation():
    customer = request.get_json()
    result = recommend(customer)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
