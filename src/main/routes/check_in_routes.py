from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_in_handler import CheckInHandler

check_in_routes = Blueprint("check_in_routes", __name__)

@check_in_routes.route("/attendees/<attendee_id>/check-ins", methods=["POST"])
def create_check_in(attendee_id):
    http_request = HttpRequest(params={"attendee_id": attendee_id})
    check_in_handler = CheckInHandler()

    response = check_in_handler.register(http_request)
    return jsonify(response.body), response.status_code