import logging

from .api import course
from .api import users
from .api import category
from .api import group
from .api import localpresentation

log = logging.getLogger(__name__)

MOODLE_WS_ENDPOINT = '/webservice/rest/server.php'

# Python3, no need for (object)
class Config:
    """
    Configuration.

    Example Usage::

    >>> import muddle
    >>> config = muddle.Config(api_key='dsghsa8casjnajk833', api_url='https://my.moodle.example.com')
    """

    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url + MOODLE_WS_ENDPOINT
        self._request_params = {'wstoken': api_key,
                               'moodlewsrestformat': 'json'}

    @property
    def request_params(self):
        return self._request_params.copy()
