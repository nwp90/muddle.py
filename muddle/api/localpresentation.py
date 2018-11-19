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

    def get_course_grade_items(self, coursename):
        """
        Get grade items in given course

        :param string coursename: The course's shortname

        Data fetched is an array of dicts with:
        :keyword integer id: grade_item id
        :keyword integer courseid: User's firstname
        :keyword string courseshortname: User's lastname
        :keyword integer categoryid: category id
        :keyword integer categoryparent: category parent id
        :keyword string categoryname: category name
        :keyword string gradename: grade item name
        :keyword string gradeitemtype: grade item type (e.g. "course", "mod")
        :keyword string grademodule: module name where itemtype is "mod"
        :keyword string gradeidnumber: external id (string) for grade item, unique per-course
        :keyword integer gradetype: ?
        :keyword integer scaleid: id of grade scale in use
        :keyword boolean scaleglobal: whether grade scale in use is global
        :keyword string scalename: name of grade scale in use
        :keyword integer sortorder: sort order for assessment within course

        Example Usage::

        >>> import muddle
        >>> muddle.localpresentation().get_course_graede_items('2018d4_GP')
        """

        params = self.config.request_params
        params.update({
            'wsfunction': 'local_presentation_get_course_grade_items',
            'course': coursename
        })
        return self.config.session.get(self.config.api_url, params=params).json()

