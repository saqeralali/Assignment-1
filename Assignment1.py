class User:
    """Represents a user who places an order."""
    def __init__(self, user_id, name, email, phone):
        self.__user_id = user_id 
        self.__name = name
        self.__email = email
        self.__phone = phone
    
    def get_user_id(self):
        return self.__user_id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def place_order(self, order):
        """Allows the user to place an order."""
        pass
    
    def cancel_order(self, order):
        """Allows the user to request order cancellation."""
        pass


class Order:
    """Represents an order with recipient and item details."""
    def __init__(self, order_id, recipient, items, status, total_cost):
        self.__order_id = order_id  
        self.__recipient = recipient 
        self.__items = items  
        self.__status = status
        self.__total_cost = total_cost
    
    def get_order_id(self):
        return self.__order_id
    
    def get_status(self):
        return self.__status
    
    def update_status(self, new_status):
        """Updates the order status (e.g., Pending, Shipped, Cancelled)."""
        self.__status = new_status
    
    def calculate_total(self):
        """Calculates the total cost of the order."""
        self.__total_cost = sum(item.get_price() for item in self.__items)
    
    def generate_delivery_note(self):
        """Generates a formatted delivery note for the order."""
        note = f"Delivery Note\nOrder ID: {self.__order_id}\nRecipient: {self.__recipient.get_name()}\nStatus: {self.__status}\nTotal Cost: {self.__total_cost} AED\nItems:\n"
        for item in self.__items:
            note += f" - {item.get_description()} (x{item.get_quantity()}): {item.get_price()} AED\n"
        return note


class Item:
    """Represents an individual item in an order."""
    def __init__(self, item_code, description, quantity, unit_price):
        self.__item_code = item_code
        self.__description = description
        self.__quantity = quantity
        self.__unit_price = unit_price
    
    def get_description(self):
        return self.__description
    
    def get_quantity(self):
        return self.__quantity
    
    def get_price(self):
        return self.__quantity * self.__unit_price


class Payment:
    """Handles payment processing for an order."""
    def __init__(self, payment_id, order_id, amount, payment_status):
        self.__payment_id = payment_id 
        self.__order_id = order_id
        self.__amount = amount
        self.__payment_status = payment_status
    
    def process_payment(self):
        """Processes the payment and updates status."""
        pass
    
    def refund_payment(self):
        """Refunds the payment if eligible."""
        pass


class Admin:
    """Represents an admin who manages orders and refunds."""
    def __init__(self, admin_id, name, role):
        self.__admin_id = admin_id  
        self.__name = name
        self.__role = role
    
    def verify_order(self, order):
        """Verifies an order before shipment."""
        pass
    
    def approve_refund(self, payment):
        """Approves or denies a refund request."""
        pass
    
    def manage_cancellations(self, order):
        """Handles order cancellation requests."""
        pass


# Creating objects to generate a delivery note
user = User(1, "Saqer Al Ali", "saqer.alali@gmail.com", "+971566630865")
items = [
    Item("ITM001", "Wireless Keyboard", 1, 100.00),
    Item("ITM002", "Wireless Mouse & Pad Set", 1, 75.00),
    Item("ITM003", "Headset", 1, 120.00),
    Item("ITM004", "Camera tripod", 3, 15.00)
]
order = Order("DEL123456789", user, items, "Pending", 0)
order.calculate_total()

delivery_note = order.generate_delivery_note()
print(delivery_note)
