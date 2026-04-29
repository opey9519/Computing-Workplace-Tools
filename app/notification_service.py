from app.models import Notification

# Availabile Services for API Endpoints


class NotificationService:
    # Initializes notification pool
    def __init__(self) -> None:
        self.notifications = []

    # Create notification and returns as dictionary
    def create(self, message) -> dict:
        notification = Notification(message)
        self.notifications.append(notification)
        return notification.to_dict()

    # Get all notifications and return in dictionary format
    def get_all(self) -> list:
        return [n.to_dict() for n in self.notifications]

    # Add Edit by id and return edited notification in dict format

    # Add Delete by id and return deleted notification
