from .processor import NotificationProcessor

class EmailProcessor(NotificationProcessor):
    def send_alert(self, message):
        print(f"Email Alert: {message}")

class SMSProcessor(NotificationProcessor):
    def send_alert(self, message):
        print(f"SMS Alert: {message}")