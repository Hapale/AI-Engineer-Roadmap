from abc import ABC, abstractmethod
from notification_request import NotificationRequest

class NotificationStrategy(ABC):

    @abstractmethod
    def send_notification(self, request: NotificationRequest):
         pass