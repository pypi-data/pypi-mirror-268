from pycloudevents import CloudEvent


def test_get_unbound_variable_from_empty_extensions():
    data = {
        "id": "12345",
        "specversion": "1.0",
        "type": "com.cloudevents.example.extension",
        "source": "https://example.com/source",
        "data": {"message": "Hello, world!"},
    }

    cloudevent = CloudEvent.from_dict(data)
    assert cloudevent.foo is None


def test_str():
    data = {
        "id": "12345",
        "specversion": "1.0",
        "type": "com.cloudevents.example.extension",
        "source": "https://example.com/source",
        "data": {"message": "Hello, world!"},
    }

    cloudevent = CloudEvent.from_dict(data)
    assert (
        str(cloudevent)
        == '<pycloudevents.CloudEvent (1.0) "com.cloudevents.example.extension" "12345" "https://example.com/source" >'
    )


def test_str__has_subject():
    data = {
        "id": "12345",
        "specversion": "1.0",
        "type": "com.cloudevents.example.extension",
        "source": "https://example.com/source",
        "data": {"message": "Hello, world!"},
        "subject": "subject_name",
    }

    cloudevent = CloudEvent.from_dict(data)
    assert (
        str(cloudevent)
        == '<pycloudevents.CloudEvent (1.0) "com.cloudevents.example.extension" "12345" "https://example.com/source" "subject_name">'
    )
