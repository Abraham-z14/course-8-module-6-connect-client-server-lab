from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# In-memory event data
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"},
]


@app.route("/", methods=["GET"])
def welcome():
    """Return a JSON welcome message."""
    return jsonify({"message": "Welcome to the Event Catalog API"}), 200


@app.route("/events", methods=["GET"])
def get_events():
    """Return all events."""
    return jsonify(events), 200


@app.route("/events", methods=["POST"])
def add_event():
    """Create and return a new event."""
    data = request.get_json(silent=True)

    # A title is required to create an event.
    if not data or not isinstance(data.get("title"), str):
        return jsonify({"error": "Title is required"}), 400

    title = data["title"].strip()

    if not title:
        return jsonify({"error": "Title is required"}), 400

    # Generate an ID one higher than the current highest ID.
    new_id = max(
        (event["id"] for event in events),
        default=0,
    ) + 1

    new_event = {
        "id": new_id,
        "title": title,
    }

    events.append(new_event)

    return jsonify(new_event), 201


@app.errorhandler(404)
def not_found(error):
    """Return JSON for unknown routes."""
    return jsonify({"error": "Resource not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)