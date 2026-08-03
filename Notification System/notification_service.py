from notification_provider import NotificationProvider
from notification_message import NotificationMessage

class NotificationService:

    def __init__(self, provider: NotificationProvider):

        self.provider = provider

    def notify(self, message: NotificationMessage):

        self.provider.notify(message)
