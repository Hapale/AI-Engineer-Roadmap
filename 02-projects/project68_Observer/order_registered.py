from eventbus import EventBus

class OrderRegistered():

    def __init__(self, order_id, total_amount):

        self.order_id = order_id
        self.total_amount = total_amount

class NotificationHandler:
    def handle(self, event):
        print(f"Confirmation notification sent for order {event.order_id}")

class InventoryHandler:
    def handle(self, event):
        print(f"The inventory of Item {event.order_id} was deducted")

class AnalyticsHandler:
    def handle(self, event):
        print(
    f"Order {event.order_id} recorded in analytics "
    f"with total amount {event.total_amount}"
)

bus = EventBus()

bus.subscribe(OrderRegistered, NotificationHandler())
bus.subscribe(OrderRegistered, InventoryHandler())
bus.subscribe(OrderRegistered, AnalyticsHandler())


#example for test

new_order_event = OrderRegistered(order_id=101, total_amount=250)
print("===Start broadcasting the event===")
bus.publish(new_order_event)
print("===End broadcasting the event===")