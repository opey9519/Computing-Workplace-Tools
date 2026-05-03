from app.models import Notification


class NotificationService:
    def __init__(self) :
        self.notifications = []
        self.next_id = 1

    def create(self, message: str):
        notification = Notification(self.next_id, message)
        self.notifications.append(notification)
        self.next_id += 1
        return notification.to_dict()

    def get_all(self):
        return [notification.to_dict() for notification in self.notifications]

    def get_by_id(self, notification_id: int):
        for notification in self.notifications:
            if notification.id == notification_id:
                return notification
        return None

    def update(self, notification_id: int, message: str):
        notification = self.get_by_id(notification_id)

        if notification is None:
            return None

        notification.message = message
        return notification.to_dict()

    def delete(self, notification_id: int):
        notification = self.get_by_id(notification_id)

        if notification is None:
            return None

        self.notifications.remove(notification)
        return notification.to_dict()