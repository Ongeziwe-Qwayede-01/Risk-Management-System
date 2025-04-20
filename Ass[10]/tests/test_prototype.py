from creational_patterns.prototype.alert_cache import AlertCache

def test_clone_alert():
    cache = AlertCache()
    cache.load()
    alert = cache.get_alert("critical")
    assert alert.severity == "high"
    assert alert.message == "System down"