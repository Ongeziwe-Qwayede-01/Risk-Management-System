class NotificationFactory:
    @staticmethod
    def create_processor(method):
        if method == "email":
            return ()
        elif method == "sms":
            return ()
        else:
            raise ValueError("Invalid method")