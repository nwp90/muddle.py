# muddle configuration file handling

import argparse
import json
import os
import requests
import logging
import http.client as http_client

MOODLE_WS_ENDPOINT = '/webservice/rest/server.php'

# Python3, no need for (object)
class WSConfig:
    """
    Configuration.

    Example Usage::

    >>> import muddle
    >>> config = muddle.config.WSConfig(api_key='dsghsa8casjnajk833', api_url='https://my.moodle.example.com')
    """

    def __init__(self, api_key=None, api_url=None, session=None, verify=None):
        self.api_key = api_key
        self.api_url = api_url + MOODLE_WS_ENDPOINT
        if session is None:
            session = requests.Session()
        if verify is not None:
            session.verify = verify
        self.session = session
        self._request_params = {
            'wstoken': api_key,
            'moodlewsrestformat': 'json'
        }

    @property
    def request_params(self):
        return self._request_params.copy()


class AppConfig():
    # argparser: fully set up argparser instance if using cli
    argparser = None
    # args: parsed args from argparser.parse_args()
    args = {}
    # conf: stored JSON config
    # _m: WSConfig for service in use

    defaults = {
        'debug': False,
        'config': os.path.join(os.path.expanduser('~'), '.mdl'),
        'service': None,
        'services': {},
        'httploglevel': 0,
        'loglevel': 'CRITICAL',
        'loggername': None,
        'requestsloglevel': 'CRITICAL',
        }

    def __init__(self):
        logging.basicConfig()
        self.add_defaults()

    def set_options(self, options):
        """ Set options if not using cli """
        self.args = options

    def cli(self, description=None):
        """ Set up args/options if using cli """
        if description is None:
            argparser = argparse.ArgumentParser()
        else:
            argparser = argparse.ArgumentParser(description=description)
        argparser.add_argument('-c', '--config', default=self.defaults['config'], help='path to JSON config file (default is ~/.mdl)')
        argparser.add_argument('-s', '--service', default=None, help='name of service to access (available services defined in config file)')
        argparser.add_argument('-d', '--debug', action='store_true', default=None, help='debug mode')
        self.argparser = argparser
        self.add_args()
        self.args = argparser.parse_args()

    # Override this in child class or call with defaults dict to add extra or update defaults if needed
    def add_defaults(self, defaults=None):
        if defaults is None:
            return
        self.defaults.update(defaults)
        return self.defaults

    # Override this in child class or just use argparser attr directly before calling cli()
    # to add extra args if needed
    def add_args(self):
        # self.argparser.add_argument(
        #     '-n', '--dryrun', action='store_true', default=False,
        #     help='dry run - check that input is valid and report on errors but do not commit'
        # )
        pass

    @property
    def logger(self):
        loggername = self.get_item('loggername')
        level = self.get_item('loglevel')
        if loggername is not None:
            log = logging.getLogger(loggername)
        else:
            log = logging.getLogger()
        if self.debug:
            log.setLevel('DEBUG')
        elif level is not None:
            log.setLevel(level)
        return log

    @property
    def requests_logger(self):
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.propagate = True
        requestslevel = self.get_item('requestsloglevel')
        if self.debug:
            requests_log.setLevel('DEBUG')
        elif requestslevel is not None:
            requests_log.setLevel(requestslevel)
        return requests_log

    def setup_httplogging(self):
        httplevel = self.get_item('httploglevel')
        if httplevel is not None:
            http_client.HTTPConnection.debuglevel = int(httplevel)

    @classmethod
    def get(cls):
        if getattr(cls, '__config', None) is None:
            cls.__config = cls()
        return cls.__config

    def usage(self):
        if self.argparser is not None:
            self.argparser.print_help()
            return True
        return False

    def error(self, msg):
        sys.stderr.write(u'ERROR: %s\n' % msg)
        if self.argparser is not None:
            self.argparser.print_help()
        sys.exit(1)

    def get_item(self, name):
        if name != 'config':
            if getattr(self, 'conf', None) is None:
                self.read_json_config()
            conf = self.conf
        else:
            conf = {}
        # global config options
        if name in ['sites', 'services']:
            key = name
        else:
            key = 'default_' + name
        var = conf.get(key, None)
        if var is None:
            var = self.defaults.get(name, None)
        if getattr(self.args, name, None) is not None:
            var = getattr(self.args, name, None)
        return var

    def read_json_config(self):
        conffile = open(self.get_item('config'))
        self.conf = json.load(conffile)
        conffile.close()
        return self.conf

    def merge_site_config(self):
        site_config = self.get_site()

    def get_site(self):
        site = self.get_item('site')
        sites = self.get_item('sites')
        if site is None:
            self.error(u'No site specified')
        site_config = sites.get(site, None)
        if site_config is None:
            self.error(u"No config available for site '%s'" % site)
        return site_config

    def get_service(self):
        service = self.get_item('service')
        services = self.get_item('services')
        if service is None:
            self.error(u'No service specified')
        service_config = services.get(service, None)
        if service_config is None:
            self.error(u"No config available for service '%s'" % service)
        return service_config

    # Return WSConfig for service in use
    @property
    def m(self):
        if getattr(self, '_m', None) is None:
            service = self.get_service()
            moodlebase = service['baseurl']
            moodletoken = service['token']
            self._m = WSConfig(moodletoken, moodlebase)
        return self._m
