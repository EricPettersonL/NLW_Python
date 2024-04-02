from flask import Blueprint, jsonify

event_routes = Blueprint("event_routes", __name__)

@event_routes.route("/events", methods=["POST"])
def create_event():
    return jsonify({"message": "Hello World"}), 200