from notification_strategy import NotificationStrategy
from notification_request import NotificationRequest

class NotificationService:
    def __init__(self, strategy:NotificationStrategy):

        self.strategy = strategy

    def send_notification(self, request:NotificationRequest):

       return self.strategy.send_notification(request)