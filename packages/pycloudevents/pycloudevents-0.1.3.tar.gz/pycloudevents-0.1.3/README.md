# PyCloudEvents

This Python library defines a CloudEvent class that represents a CloudEvent object according to the [CloudEvents specification](https://www.cncf.io/projects/cloudevents/).

## TOC

- [PyCloudEvents](#pycloudevents)
  - [TOC](#toc)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Creating a CloudEvent object](#creating-a-cloudevent-object)
    - [Serializing a CloudEvent object to JSON](#serializing-a-cloudevent-object-to-json)
    - [Deserializing a JSON string to a CloudEvent object](#deserializing-a-json-string-to-a-cloudevent-object)
  - [CloudEvent Attributes](#cloudevent-attributes)
  - [Contributing](#contributing)

## Installation

```shell
pip install pycloudevents
```

## Usage

The `CloudEvent` class provides methods to create, serialize (convert to JSON), and deserialize CloudEvents.

### Creating a CloudEvent object

There are four ways to create a `CloudEvent` object:

Using keyword arguments in the constructor:

```python
from pycloudevents import CloudEvent

event = CloudEvent(
    id="my-id",
    source="https://example.com/source",
    type="com.cloudevents.example.extension",
    data={"message": "Hello, world!"},
)
```

From a dictionary:

```python
from pycloudevents import CloudEvent

data = {
    "id": "12345",
    "specversion": "1.0",
    "type": "com.cloudevents.example.extension",
    "source": "https://example.com/source",
    "data": {"message": "Hello, world!"},
}

event = CloudEvent.from_dict(data)
```

From a mapping object:

```python
from pycloudevents import CloudEvent

data = {
    "id": "12345",
    "specversion": "1.0",
    "type": "com.cloudevents.example.extension",
    "source": "https://example.com/source",
    "data": {"message": "Hello, world!"},
}

event = CloudEvent.from_mapping(data)
```

From a JSON string:

```python
from pycloudevents import CloudEvent

json_string = '{"id": "12345", "specversion": "1.0", "type": "com.cloudevents.example.extension", "source": "https://example.com/source", "data": {"message": "Hello, world!"}}'

event = CloudEvent.from_json(json_string)
```

### Serializing a CloudEvent object to JSON

The `to_structured` method converts a `CloudEvent` object to a JSON string:

```python
from pycloudevents import CloudEvent

event = CloudEvent(...)  # Create an event object

json_data = event.to_structured()
print(json_data)
```

### Deserializing a JSON string to a CloudEvent object

The `from_json` class method creates a `CloudEvent` object from a JSON string:

```python
from pycloudevents import CloudEvent

json_string = '{"specversion": "1.0", ...}'  # Your JSON string

event = CloudEvent.from_json(json_string)
```

## CloudEvent Attributes

The `CloudEvent` class includes the following attributes according to the CloudEvents specification:

- `id`: (str) The identifier of the event.
- `source`: (str) The source of the event.
- `specversion`: (str) The CloudEvents specification version (default is "1.0").
- `type`: (str) The type of the event.
- `datacontenttype`: (Optional[str]) The data content type (default is None).
- `dataschema`: (Optional[str]) The data schema (default is None).
- `subject`: (Optional[str]) The subject of the event (default is None).
- `time`: (Optional[str]) The timestamp of the event (default is None).
- `data`: (Any) The data associated with the event (default is None).
- `extensions`: (Hashable) Additional extensions for the event.

## Contributing

See more in our [Contributing Guidelines](./CONTRIBUTING.md)
