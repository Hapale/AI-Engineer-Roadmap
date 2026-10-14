from notification_strategy import NotificationStrategy
from notification_request import NotificationRequest


class PushNotification(NotificationStrategy):

    def send_notification(self, request: NotificationRequest):

        receiver = request.receiver
        message = request.message

        return f"Push sent to {receiver}: {message}"


