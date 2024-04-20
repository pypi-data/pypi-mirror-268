# Standard Library
from typing import Optional, Union

# Third-Party Libraries
import requests


class OpenExchangeError(Exception):
    pass


class APIError(OpenExchangeError):
    message: str
    request: Union[requests.Request, requests.models.PreparedRequest]

    body: Optional[object]
    """The API response body.

    If the API responded with a valid JSON structure then this property will be the
    decoded result.

    If it isn't a valid JSON structure then this will be the raw response.

    If there was no response associated with this error then it will be `None`.
    """

    def __init__(
        self, message: str, request: Union[requests.Request, requests.models.PreparedRequest], *, body: Optional[object]
    ) -> None:
        super().__init__(message)
        self.request = request
        self.message = message
        self.body = body
