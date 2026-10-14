from notification_strategy import NotificationStrategy
from notification_request import NotificationRequest


class WhatsAppNotification(NotificationStrategy):

    def send_notification(self, request: NotificationRequest):

        receiver = request.receiver
        message = request.message

        return f"WhatsApp sent to {receiver}: {message}"



