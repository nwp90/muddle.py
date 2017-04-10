import logging

import .course
import .category
import .group


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
        self.request_params = {'wstoken': api_key,
                               'moodlewsrestformat': 'json'}

