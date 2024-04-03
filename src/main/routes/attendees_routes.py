from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendees_routes = Blueprint("attendees_routes", __name__)

@attendees_routes.route("/events/<event_id>/register", methods=["POST"])
def register_attendee(event_id):
    http_request = HttpRequest(params={"event_id": event_id}, body=request.json)
    attendees_handler = AttendeesHandler()

    response = attendees_handler.register(http_request)
    return jsonify(response.body), response.status_code


@attendees_routes.route("/attendees/<attendee_id>/badge", methods=["GET"])
def find_attendee_badge(attendee_id):
    http_request = HttpRequest(params={"attendee_id": attendee_id})
    attendees_handler = AttendeesHandler()

    response = attendees_handler.find_attendee_badge(http_request)
    return jsonify(response.body), response.status_code


@attendees_routes.route("/events/<event_id>/attendees", methods=["GET"])
def find_attendees_from_event(event_id):
    http_request = HttpRequest(params={"event_id": event_id})
    attendees_handler = AttendeesHandler()

    response = attendees_handler.find_attendees_from_event(http_request)
    return jsonify(response.body), response.status_code