from notification_strategy import NotificationStrategy
from notification_request import NotificationRequest

class EmailNotification(NotificationStrategy):

    def send_notification(self, request: NotificationRequest):
        receiver = request.receiver
        message = request.message
        title = request.title

        title_part = f"{title} - " if title else ""             #برای این که اگر خالی بود جاش فضای خالی باشه نه None
        return f"Email sent to {receiver}: {title_part}{message}"


