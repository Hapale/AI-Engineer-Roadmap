from abc import ABC, abstractmethod

from notification_message import NotificationMessage


class NotificationProvider(ABC):

    @abstractmethod
    def notify(self, message: NotificationMessage) -> None:
        """Send a notification."""
        raise NotImplementedError