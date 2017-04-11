import requests
from muddle.utils import valid_options, clean_username

class API:
    """ Represents API endpoints for Moodle Users """

    def __init__(self, config):
        self.config = config

    def get_users_by_field(self, fieldname, values, clean=True):
        """
        Get users with field matching values

        :param string field: 'id', 'idnumber', 'username' or 'email'
        :param list values: a list of values to match

        Returns:

        :param list : a list of user descriptions, each of which has the following fields:

        :param int id: ID of the user
        :param string username: the username
        :param string firstname: The first name(s) of the user
        :param string lastname: The family name of the user
        :param string fullname: The fullname of the user
        :param string email: An email address - allow email as root@localhost
        :param string address: Postal address
        :param string phone1: Phone 1
        :param string phone2: Phone 2
        :param string icq: icq number
        :param string skype: skype id
        :param string yahoo: yahoo id
        :param string aim: aim id
        :param string msn: msn number
        :param string department: department
        :param string institution: institution
        :param string idnumber: An arbitrary ID code number perhaps from the institution
        :param string interests: user interests (separated by commas)
        :param string firstaccess: first access to the site (0 if never)
        :param string lastaccess: last access to the site (0 if never)
        :param string auth: Auth plugins include manual, ldap, imap, etc
        :param ??? suspended: Suspend user account, either false to enable user login or true to disable it
        :param ??? confirmed: Active user: 1 if confirmed, 0 otherwise
        :param string lang: Language code such as "en", must exist on server
        :param string calendartype: Calendar type such as "gregorian", must exist on server
        :param string theme: Theme name such as "standard", must exist on server
        :param string timezone: Timezone code such as Australia/Perth, or 99 for default
        :param ??? mailformat: Mail format code is 0 for plain text, 1 for HTML etc
        :param string description: User profile description
        :param string descriptionformat: descriptionformat
        :param string city: Home city of the user
        :param string url: URL of the user
        :param string country: ISO 2-letter code for home country of the user, such as AU or CZ
        :param string profileimageurlsmall: User image profile URL - small version
        :param string profileimageurl: User image profile URL - big version
        :param list customfields: List of custom profile fields, each having 'type', 'value', 'name', 'shortname'
        :param list preferences: List of preferences, each having 'name' and 'value'
        """
        
        option_params = { 'field': fieldname }
        for (index, value) in enumerate(values):
            if (clean and (fieldname == 'username')):
                value = clean_username(value)
            option_params['values[' + str(index) + ']'] = value

        params = {'wsfunction': 'core_user_get_users_by_field'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.get(self.config.api_url, params=params, verify=False).json()
