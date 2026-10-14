from email_notification import EmailNotification
from sms_notification import SMSNotification
from push_notification import PushNotification
from whatsapp_notification import WhatsAppNotification


class NotificationFactory():

    def create_notification(self,notification_type):

    
        if notification_type == "email":
            strategy = EmailNotification()
        elif notification_type == "sms":
            strategy = SMSNotification()
        elif notification_type == "push":
            strategy = PushNotification()
        elif notification_type == "whatsapp":
            strategy = WhatsAppNotification()
        else:
            raise ValueError("Invalid notification type")

        return strategy
     
