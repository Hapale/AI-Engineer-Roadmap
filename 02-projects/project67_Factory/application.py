from notification_request import NotificationRequest
from notification_factory import NotificationFactory
from notification_service import NotificationService


class Application:
    def handle_request(self, notification_type: str, receiver: str, message: str, title: str) -> str :

        try:
            notification_request = NotificationRequest(receiver, message, title)

            factory = NotificationFactory()
            strategy = factory.create_notification(notification_type)

            notification_service = NotificationService(strategy)
            result = notification_service.send_notification(notification_request)

            return result
            
        except ValueError as e:
            return f"error: {e}"
    
        