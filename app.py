from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Simple Data API is running!"


@app.route("/sum", methods=["POST"])
def calculate_sum():
    data = request.get_json()

    numbers = data.get("numbers", [])

    if not numbers:
        return jsonify({"error": "No numbers provided"}), 400

    total = sum(numbers)

    return jsonify({
        "numbers": numbers,
        "sum": total
    })


@app.route("/stats", methods=["POST"])
def calculate_stats():
    data = request.get_json()

    numbers = data.get("numbers", [])

    if not numbers:
        return jsonify({"error": "No numbers provided"}), 400

    result = {
        "count": len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)