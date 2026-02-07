from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Simple Data API is running!"


@app.route("/sum", methods=["POST"])
def calculate_sum():
    try:
        data = request.get_json()

        if not data or "numbers" not in data:
            return jsonify({"error": "Invalid input format"}), 400

        numbers = data["numbers"]

        if not isinstance(numbers, list):
            return jsonify({"error": "Numbers must be a list"}), 400

        total = sum(numbers)

        return jsonify({
            "numbers": numbers,
            "sum": total
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/stats", methods=["POST"])
def calculate_stats():
    try:
        data = request.get_json()

        if not data or "numbers" not in data:
            return jsonify({"error": "Invalid input format"}), 400

        numbers = data["numbers"]

        if not isinstance(numbers, list):
            return jsonify({"error": "Numbers must be a list"}), 400

        result = {
            "count": len(numbers),
            "max": max(numbers),
            "min": min(numbers),
            "average": sum(numbers) / len(numbers)
        }

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500
        
    result = {
        "count": len(numbers),
        "max": max(numbers),
        "min": min(numbers),
        "average": sum(numbers) / len(numbers)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)