from pycloudevents import CloudEvent

event = CloudEvent(
    id="my-id",
    source="https://example.com/source",
    type="com.cloudevents.example.extension",
    data={"message": "Hello, world!"},
)

data = {
    "id": "12345",
    "specversion": "1.0",
    "type": "com.cloudevents.example.extension",
    "source": "https://example.com/source",
    "data": {"message": "Hello, world!"},
}

event = CloudEvent.from_dict(data)

json_string = '{"id": "12345", "specversion": "1.0", "type": "com.cloudevents.example.extension", "source": "https://example.com/source", "data": {"message": "Hello, world!"}}'

event = CloudEvent.from_json(json_string)
