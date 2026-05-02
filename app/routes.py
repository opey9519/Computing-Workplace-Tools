from flask import Blueprint, request, jsonify
from app.notification_service import NotificationService

main = Blueprint("main", __name__)
service = NotificationService()


@main.route("/", methods=["GET"])
def home():
    return jsonify({"message": "CI/CD Notification System Running"}), 200


@main.route("/notifications", methods=["GET"])
def get_notifications():
    notifications = service.get_all()
    return jsonify(notifications), 200


@main.route("/notifications", methods=["POST"])
def create_notification():
    data = request.get_json()

    if not data or "message" not in data or not data["message"].strip():
        return jsonify({"error": "Message is required"}), 400

    notification = service.create(data["message"].strip())
    return jsonify(notification), 201


@main.route("/notifications/<int:notification_id>", methods=["PUT"])
def edit_notification(notification_id):
    data = request.get_json()

    if not data or "message" not in data or not data["message"].strip():
        return jsonify({"error": "Message is required"}), 400

    notification = service.update(notification_id, data["message"].strip())

    if notification is None:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify(notification), 200


@main.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    notification = service.delete(notification_id)

    if notification is None:
        return jsonify({"error": "Notification not found"}), 404

    return jsonify({
        "message": "Notification deleted",
        "notification": notification
    }), 200