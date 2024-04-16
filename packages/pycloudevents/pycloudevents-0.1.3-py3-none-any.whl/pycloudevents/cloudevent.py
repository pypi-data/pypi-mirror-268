from copy import deepcopy
from datetime import datetime
import json
from typing import Any, Dict, Hashable, Literal, Mapping, Optional
from pycloudevents.exceptions import ValidationError


class CloudEvent:
    def __init__(
        self,
        *,
        id: str,
        source: str,
        specversion: Literal["1.0"] = "1.0",
        type: str,
        datacontenttype: Optional[str] = "application/json",
        dataschema: Optional[str] = None,
        subject: Optional[str] = None,
        time: Optional[str] = None,
        data: Any = None,
        **extensions: Hashable,
    ) -> None:
        """
        Initialize the class with the provided parameters.

        Parameters:
            id (str): The identifier for the object.
            source (str): The source of the object.
            specversion (str): The specification version (default is "1.0").
            type (str): The type of the object.
            datacontenttype (Optional[str]): The content type of the data (default is None).
            dataschema (Optional[str]): The schema of the data (default is None).
            subject (Optional[str]): The subject of the object (default is None).
            time (Optional[str]): The timestamp of the object (default is None).
            data (Any): The data associated with the object (default is None).
            **extensions (Hashable): Additional extensions for the object.
        Returns:
            None
        """
        self._id = id
        self._source = source
        self._specversion = specversion
        self._type = type
        self._datacontenttype = datacontenttype
        self._dataschema = dataschema
        self._subject = subject
        self._time = time
        self._data = data
        self._extensions = extensions

        self._validation_errors: list[str] = []

    def __getattr__(self, name: str) -> Any:
        attr = self._extensions.get(name)
        return attr

    @property
    def id(self) -> str:
        return self._id

    @property
    def specversion(self) -> str:
        return self._specversion

    @property
    def source(self) -> str:
        return self._source

    @property
    def type(self) -> str:
        return self._type

    @property
    def datacontenttype(self) -> Optional[str]:
        return self._datacontenttype

    @property
    def dataschema(self) -> Optional[str]:
        return self._dataschema

    @property
    def subject(self) -> Optional[str]:
        return self._subject

    @property
    def time(self) -> Optional[str]:
        return self._time

    @property
    def data(self) -> Any:
        return self._data

    def _is_validated(self) -> bool:
        self._validation_errors.clear()

        # Spec version
        if not self._specversion == "1.0":
            self._validation_errors.append("specversion must be 1.0")

        # Required fields
        if self._id is None:
            self._validation_errors.append("id must not be None")
        if self._source is None:
            self._validation_errors.append("source must not be None")
        if self._type is None:
            self._validation_errors.append("type must not be None")

        # Check format
        if isinstance(self._time, str):
            # TODO: Switch to check for ISO 3339 format
            try:
                datetime.fromisoformat(self._time)
            except ValueError:
                self._validation_errors.append("time must be in ISO8601 format")

        if self._validation_errors:
            return False
        return True

    def to_structured(self, *args, **kwargs):
        """
        A function that converts the object attributes into a JSON format.

        Parameters:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            str: A JSON string representing the object attributes.
        """
        v = {
            "id": self._id,
            "source": self._source,
            "specversion": self._specversion,
            "type": self._type,
            "data": self._data,
            **self._extensions,
        }
        if self._datacontenttype is not None:
            v["datacontenttype"] = self._datacontenttype
        if self._dataschema is not None:
            v["dataschema"] = self._dataschema
        if self._subject is not None:
            v["subject"] = self._subject
        if self._time is not None:
            v["time"] = self._time
        return json.dumps(v, *args, **kwargs)

    def to_json(self, *args, **kwargs):
        return self.to_structured(*args, **kwargs)

    @classmethod
    def from_json(cls, json_str: str, *args, **kwargs):
        """
        Class method to create an instance from a JSON string.

        Args:
            json_str (str): The JSON string to parse.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The instance created from the JSON string.
        """
        v: dict[str, Any] = json.loads(json_str, *args, **kwargs)
        return cls.from_dict(v)

    @classmethod
    def from_mapping(cls, m: Mapping[str, Any]):
        """
        Create an instance of the class from a mapping, using the provided mapping as the initial data.

        Args:
            m (Mapping[str, Any]): A mapping of string keys to values of any type.

        Returns:
            An instance of the class.
        """
        v = deepcopy(m)
        return cls.from_dict(dict(v))

    @classmethod
    def from_dict(cls, v: Dict[str, Any]):
        """
        Generate an instance from a dictionary.

        Parameters:
            v (Dict[str, Any]): A dictionary containing the data for the instance.

        Returns:
            An instance created from the dictionary data.
        """
        id_ = v.pop("id")
        source = v.pop("source")
        type_ = v.pop("type")
        obj = cls(
            id=id_,
            source=source,
            type=type_,
            **v,
        )
        if not obj._is_validated():
            raise ValidationError(obj._validation_errors)
        return obj


if __name__ == "__main__":
    v = {
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
    event = CloudEvent.from_mapping(v)
    print(event.to_json())
    print(v)
