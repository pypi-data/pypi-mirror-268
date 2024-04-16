from pycloudevents import CloudEvent


def test_create_from_dict():
    dict_ = {
        "specversion": "1.0",
        "type": "com.github.pull_request.opened",
        "source": "https://github.com/cloudevents/spec/pull",
        "subject": "123",
        "id": "A234-1234-1234",
        "time": "2018-04-05T17:31:00Z",
        "comexampleextension1": "value",
        "comexampleothervalue": 5,
        "datacontenttype": "text/xml",
        "data": '<much wow="xml"/>',
    }
    event = CloudEvent.from_dict(dict_)
    for key in dict_:
        assert getattr(event, key) == dict_[key]
    for attr in ("id", "type", "source"):
        assert attr not in dict_


def test_create_from_mapping():
    dict_ = {
        "specversion": "1.0",
        "type": "com.github.pull_request.opened",
        "source": "https://github.com/cloudevents/spec/pull",
        "subject": "123",
        "id": "A234-1234-1234",
        "time": "2018-04-05T17:31:00Z",
        "comexampleextension1": "value",
        "comexampleothervalue": 5,
        "datacontenttype": "text/xml",
        "data": '<much wow="xml"/>',
    }
    event = CloudEvent.from_mapping(dict_)
    for key in dict_:
        assert getattr(event, key) == dict_[key]
    for attr in ("id", "type", "source"):
        assert attr in dict_
