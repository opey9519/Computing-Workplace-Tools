class Notification:
    def __init__(self, notification_id: int, message: str):
        self.id = notification_id
        self.message = message

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "message": self.message
        }