from notification_strategy import NotificationStrategy
from notification_request import NotificationRequest


class SMSNotification(NotificationStrategy):

    def send_notification(self, request: NotificationRequest):

        receiver = request.receiver
        message = request.message

        return f"SMS sent to {receiver}: {message}"
