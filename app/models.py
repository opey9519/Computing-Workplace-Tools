# Notification Model for MongoDB DB if we implement

class Notification:
    def __init__(self, message) -> None:
        self.message = message

    def to_dict(self) -> dict:
        return {
            "message": self.message
        }
