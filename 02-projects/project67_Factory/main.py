from application import Application

def get_user_input():
    print("=====Set your notification type=====")

    notification_type = input("Set your notification type (Email/SMS/Push/Whatsapp):").strip().lower()

    try:
        receiver = input("Receiver :")
        message = str(input("Message :"))
        title = str(input("Title :"))
    except ValueError:
        return None, None, None, None, "Error : Most enter true"

    return notification_type, receiver, message, title

if __name__== "__main__":

    app = Application()

    notification_type, receiver, message, title = get_user_input()

    result = app.handle_request(notification_type, receiver, message, title)

    print(result)
