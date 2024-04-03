from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.event_handler import EventHandler


event_routes = Blueprint("event_routes", __name__)

@event_routes.route("/events", methods=["POST"])
def create_event():
    http_request = HttpRequest(body=request.json)
    event_handler = EventHandler()
    
    response = event_handler.register(http_request)
    return jsonify(response.body), response.status_code

@event_routes.route("/events/<event_id>", methods=["GET"])
def get_event(event_id):
    http_request = HttpRequest(params={"event_id": event_id})
    event_handler = EventHandler()
    
    response = event_handler.find_by_id(http_request)
    return jsonify(response.body), response.status_code