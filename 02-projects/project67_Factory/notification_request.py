class NotificationRequest:

    def __init__(self, receiver: str, message: str, title: str = None):

        if receiver is None or not  receiver.strip():
            raise ValueError("The receiver cannot be empty or contain spaces.")
        if message is None or not message.strip():
            raise ValueError("The message cannot be empty or contain spaces.")


        self.receiver = receiver.strip()
        self.message = message.strip()
        self.title = title.strip() if title is not None else None
        