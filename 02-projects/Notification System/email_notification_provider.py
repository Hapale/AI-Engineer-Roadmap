from notification_provider import NotificationProvider
from notification_message import NotificationMessage

class EmailNotificationProvider(NotificationProvider):
        
    def notify(self, message: NotificationMessage):

        print("Sending email...")