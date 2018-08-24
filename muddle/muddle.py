import logging
import requests

from .api import course
from .api import users
from .api import category
from .api import group
from .api import localpresentation
from .api import stats

from .config import WSConfig as WSConfig
from .config import AppConfig as AppConfig

log = logging.getLogger(__name__)

MOODLE_WS_ENDPOINT = '/webservice/rest/server.php'

# Backwardly compatible
Config = WSConfig
