from flask import Blueprint, request, jsonify
from app.notification_service import NotificationService

main = Blueprint("main", __name__)
service = NotificationService()

# Ensures app is running


@main.route("/", methods=["GET"])
def home():
    return jsonify({"message": "CI/CD Notification System Running"}), 200

# Get all notifications


# @main.route("/notifications", methods=["GET"])
# def get_notifications():
#     notifications = service.get_all()
#     return jsonify(notifications), 200

# # Create notification


# @main.route("/notifications", methods=["POST"])
# def create_notification():
#     data = request.get_json()

#     if not data or "message" not in data:
#         return jsonify({"error": "Message is required"}), 400

#     notification = service.create(data["message"])
#     return jsonify(notification), 201


# @main.route("/notifications/<int:id>", methods=["PUT"])
# def edit_notification(id):
#     pass


# @main.route("/notifications/<int:id>", methods=["DELETE"])
# delete_notification(id):
#     pass
