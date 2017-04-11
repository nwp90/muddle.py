import requests
from muddle.utils import valid_options


class API:
    """ Represents API endpoints for Moodle Groups """

    def __init__(self, config):
        self.config = config

    def create_groups(self, groups):
        """

        Create new group(s)

        :param list groups: list of new groups, each of which is specified by a \
            dict containing:
         :param int courseid: id of course in which to create group.
         :param string name: name of group to be created.
         :param string description: description of group to be created.
         :param int descriptionformat: Format of description field, format options currently 1=FORMAT_HTML, 2=FORMAT_PLAIN, 3=FORMAT_WIKI, 4=FORMAT_MARKDOWN
         :param string enrolmentkey: (optional) Passphrase to allow joining group.
         :param int idnumber: (optional) id number. Probably for matching external systems?

        Returns a list of the groups created, with the same fields as above and the
        new group id added as 'id'.

        Example Usage::

        >>> import muddle
        >>> muddle.category().create('category name')
        """
        group_options = [
            'courseid',
            'name',
            'description',
            'descriptionformat',
            'enrolmentkey',
            'idnumber'
        ]

        option_params = {}
        for i, group in enumerate(groups):
            if valid_options(group, group_options):
                for key in group:
                    option_params.update({
                        'groups[%s][%s]' % (i, key): str(kwargs.get(key))
                    })
        params = {'wsfunction': 'core_group_create_groups'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False).json()

    def get_groups(self, idlist):
        """
        Fetch group data for specified group ids.
        
        Data fetched is as per create_groups.
        """
        params = self.config.request_params
        params.update({
            'wsfunction': 'core_group_get_groups',
            'ids': idlist
        })
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def get_course_groups(self, course_id):
        """
        Fetch groups for specified course id.
        
        Data fetched is as per create_groups, but with the addition of 'id' for
        each group.
        """
        params = self.config.request_params
        params.update({
            'wsfunction': 'core_group_get_course_groups',
            'courseid': course_id
        })
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def delete_groups(self, idlist):
        """
        Deletes specified groups. Returns nothing.

        Example Usage::

        >>> import muddle
        >>> muddle.course(10).delete()
        """
        option_params = {}
        for i, groupid in enumerate(idlist):
            option_params.update({
                'groupids[%s]' % i: groupid
            })
        params = {'wsfunction': 'core_group_delete_groups'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

    def get_group_members(self, idlist):
        """
        Fetch group members for specified group ids.
        
        Returns a list of dicts with 'groupid' and 'userids' entries. 'userids'
        value is a list of user ids.
        """
        option_params = {}
        for i, groupid in enumerate(idlist):
            option_params.update({
                'groupids[%s]' % i: groupid
            })
        params = {'wsfunction': 'core_group_get_group_members'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def add_group_members(self, members):
        """
        Add users to groups.

        Parameter is a list of dicts with keys 'groupid' and 'userid'; specified
        users will be added to specified groups.
        
        Returns nothing.
        """
        option_params = {}
        for i, member in enumerate(members):
            option_params.update({
                'members[%s][groupid]' % i: member['groupid'],
                'members[%s][userid]' % i: member['userid']
            })
        params = {'wsfunction': 'core_group_add_group_members'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

    def delete_group_members(self, members):
        """
        Delete users from groups.

        Parameter is a list of dicts with keys 'groupid' and 'userid'; specified
        users will be removed from specified groups.
        
        Returns nothing.
        """
        option_params = {}
        for i, member in enumerate(members):
            option_params.update({
                'members[%s][groupid]' % i: member['groupid'],
                'members[%s][userid]' % i: member['userid']
            })
        params = {'wsfunction': 'core_group_delete_group_members'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

    def create_groupings(self, groupings):
        """

        Create new grouping(s). A grouping is basically a group of groups.

        :param list groupings: list of new groupings, each of which is specified by a \
            dict containing:
         :param int courseid: id of course in which to create grouping.
         :param string name: name of grouping to be created.
         :param string description: description of grouping to be created.
         :param int descriptionformat: Format of description field, format options currently 1=FORMAT_HTML, 2=FORMAT_PLAIN, 3=FORMAT_WIKI, 4=FORMAT_MARKDOWN
         :param int idnumber: (optional) id number. Probably for matching external systems?

        Returns a list of the groupings created, with the same fields as above and
        the new grouping id added as 'id'.

        Example Usage::

        >>> import muddle
        >>> muddle.category().create('category name')
        """
        grouping_options = [
            'courseid',
            'name',
            'description',
            'descriptionformat',
            'idnumber'
        ]

        option_params = {}
        for i, grouping in enumerate(groupings):
            if valid_options(grouping, grouping_options):
                for key in grouping:
                    option_params.update({
                        'groupings[%s][%s]' % (i, key): str(kwargs.get(key))
                    })
        params = {'wsfunction': 'core_group_create_groupings'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False).json()

    def update_groupings(self, groupings):
        """

        Update existing grouping(s). A grouping is basically a group of groups.

        :param list groupings: list of groupings, each of which is specified by a \
            dict containing:
         :param int id: id of grouping to update.
         :param string name: new name of grouping.
         :param string description: new description of grouping.
         :param int descriptionformat: Format of description field, format options currently 1=FORMAT_HTML, 2=FORMAT_PLAIN, 3=FORMAT_WIKI, 4=FORMAT_MARKDOWN
         :param int idnumber: (optional) id number. Probably for matching external systems?

        Returns nothing.

        Example Usage::

        >>> import muddle
        >>> muddle.category().create('category name')
        """
        grouping_options = [
            'id',
            'name',
            'description',
            'descriptionformat',
            'idnumber'
        ]

        option_params = {}
        for i, grouping in enumerate(groupings):
            if valid_options(grouping, grouping_options):
                for key in grouping:
                    option_params.update({
                        'groupings[%s][%s]' % (i, key): str(kwargs.get(key))
                    })
        params = {'wsfunction': 'core_group_update_groupings'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

    def get_groupings(self, idlist, returngroups=True):
        """
        Fetch grouping details for specified grouping ids.
        
        Returns a list of dicts as per params to update_groupings, but with
        addition of 'groups' key for each grouping. 'groups' value is a list
        of dicts representing groups, as per get_groups.

        'groups' key is only populated if 'returngroups' param is True.
        """
        option_params = {}
        for i, groupingid in enumerate(idlist):
            option_params.update({
                'groupingids[%s]' % i: groupingid
            })
        params = {
            'wsfunction': 'core_group_get_groupings',
            'returngroups': 1 if returngroups else 0
        }
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def get_course_groupings(self, course_id):
        """
        Fetch groupings for specified course id.
        
        Data fetched is as per that supplied to update_groupings.
        Groups belonging to groupings are not retrieved.
        """
        params = self.config.request_params
        params.update({
            'wsfunction': 'core_group_get_course_groupings',
            'courseid': course_id
        })
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def delete_groupings(self, idlist):
        """
        Deletes specified groupings. Returns nothing.

        Example Usage::

        >>> import muddle
        >>> muddle.course(10).delete()
        """
        option_params = {}
        for i, groupingid in enumerate(idlist):
            option_params.update({
                'groupingids[%s]' % i: groupingid
            })
        params = {'wsfunction': 'core_group_delete_groupings'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

    def assign_grouping(self, assignments):
        """
        Assign groups to groupings.

        Parameter is a list of dicts with keys 'groupingid' and 'groupid'; specified
        groups will be added to specified groupings.
        
        Returns nothing.
        """
        option_params = {}
        for i, assignment in enumerate(assignments):
            option_params.update({
                'assignments[%s][groupingid]' % i: assignment['groupingid'],
                'assignments[%s][groupid]' % i: assignment['groupid']
            })
        params = {'wsfunction': 'core_group_assign_grouping'}
        params.update(option_params)
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

