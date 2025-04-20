# notification_base.py
class NotificationProcessor:
    @staticmethod
    def create_processor(method):
        from .payment_processor import EmailProcessor, SMSProcessor  # Late import to avoid circular import

        if method == "email":
            return EmailProcessor()
        elif method == "sms":
            return SMSProcessor()
        else:
            raise ValueError("Invalid method")
