from muddle.utils import valid_options

class API:
    """ Represents API endpoints for the local_presentation plugin """

    def __init__(self, config):
        self.config = config

    def get_course_role_users(self, coursename, rolename):
        """
        Get users in given role in given course

        :param string coursename: The course's shortname
        :param string rolename: The role's shortname

        Data fetched is an array of dicts with:
        :keyword string username: User's username
        :keyword string firstname: User's firstname
        :keyword string lastname: User's lastname
        :keyword string email: User's email

        Example Usage::

        >>> import muddle
        >>> muddle.localpresentation().get_course_role_users('2018d4_GP', 'convenor')
        """

        params = self.config.request_params
        params.update({
            'wsfunction': 'local_presentation_get_course_role_users',
            'course': coursename,
            'role': rolename,
        })
        return self.config.session.post(self.config.api_url, params=params).json()
