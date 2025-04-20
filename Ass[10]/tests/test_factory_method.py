from creational_patterns import NotificationFactory

def test_email_processor():
    processor = NotificationFactory.create_processor("email")
    assert processor.__class__.__name__ == "EmailProcessor"

def test_sms_processor():
    processor = NotificationFactory.create_processor("sms")
    assert processor.__class__.__name__ == "SMSProcessor"