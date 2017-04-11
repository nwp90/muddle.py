import requests
from muddle.utils import valid_options

class API:
    """ Represents API endpoints for a Moodle Course """

    def __init__(self, config):
        self.config = config

    def create_courses(self, fullname, shortname, category_id, **kwargs):
        """
        Create a new course

        :param string fullname: The course's fullname
        :param string shortname: The course's shortname
        :param int category_id: The course's category

        :keyword string idnumber: (optional) Course ID for matching with external systems.
        :keyword string summary: (optional) Course summary text.
        :keyword int summaryformat: (optional) Defaults to 1 (HTML). \
            Summary format options currently 1=FORMAT_HTML, 2=FORMAT_PLAIN, 3=FORMAT_WIKI, 4=FORMAT_MARKDOWN
        :keyword string format: (optional) Defaults to "topics"
            Topic options: (weeks, topics, social, site)
        :keyword bool showgrades: (optional) Defaults to True. \
            Determines if grades are shown
        :keyword int newsitems: (optional) Defaults to 5. \
            Number of recent items appearing on the course page
        :keyword int startdate: (optional) Timestamp when the course starts.
        :keyword int enddate: (optional) Timestamp when the course ends.
        :keyword int numsections: (deprecated) number of weeks/topics in course.
        :keyword int maxbytes: (optional) Defaults to 83886080. \
            Largest size of file that can be uploaded into the course
        :keyword bool showreports: Default to True. Are activity report shown?
        :keyword bool visible: (optional) Determines if course is \
            visible to students
        :keyword int hiddensections: (deprecated) How any hidden sections in the course are displayed. Use courseformatoptions instead.
        :keyword int groupmode: (optional) Defaults to 2.
            options: (0 = no group, 1 = separate, 2 = visible)
        :keyword bool groupmodeforce: (optional) Defaults to False. \
            Force group mode
        :keyword int defaultgroupingid: (optional) Defaults to 0. \
            Default grouping id
        :keyword bool enablecompletion: (optional) Enable control via \
            completion in activity settings.
        :keyword bool completionnotify: (optional) Default? Dunno. \
            Presumably notifies course completion
        :keyword string lang: (optional) Force course language.
        :keyword string forcetheme: (optional) Name of the force theme
        :keyword list courseformatoptions: (optional) Additional options for the selected course format, a list of dicts with 'name' & 'value' as keys.

        Missing from API:
        :keyword int categorysortorder: sort order into the category
        
        Example Usage::

        >>> import muddle
        >>> muddle.course().create('a new course', 'new-course', 20)
        """

        allowed_options = ['idnumber', 'summary', 'summaryformat',
                           'format', 'showgrades',
                           'newsitems', 'startdate', 'enddate',
                           'numsections', 'maxbytes', 'showreports',
                           'visible', 'hiddensections', 'groupmode',
                           'groupmodeforce', 'defaultgroupingid',
                           'enablecompletion', 'completionnotify', 'lang',
                           'forcetheme', 'courseformatoptions']

        if valid_options(kwargs, allowed_options):
            option_params = {}
            for index, key in enumerate(kwargs):
                val = kwargs.get(key)
                if isinstance(val, bool):
                    val = int(val)
                option_params.update({'courses[0][' + key + ']': val})

            params = {'wsfunction': 'core_course_create_courses',
                      'courses[0][fullname]': fullname,
                      'courses[0][shortname]': shortname,
                      'courses[0][categoryid]': category_id}
            params.update(option_params)
            params.update(self.config.request_params)
            return requests.post(self.config.api_url, params=params, verify=False)

    def get_courses(self, idlist):
        """
        Fetch course data for specified course ids.
        
        Data fetched:
        :keyword int id: course id
        :keyword string shortname: course short name
        :keyword int categoryid: id of category containing course
        :keyword int categorysortorder: sort order into the category
        :keyword string fullname: course full name
        :keyword string displayname: course display name
        :keyword string idnumber: id number (for matching with external systems, never used within Moodle)
        :keyword string summary: course summary
        :keyword int summaryformat: format of summary (currently 1=FORMAT_HTML, 2=FORMAT_PLAIN, 3=FORMAT_WIKI, 4=FORMAT_MARKDOWN)
        :keyword string format: formatting plugin used for this course e.g. topics, social, site...
        :keyword int showgrades: 1 if grades are shown, otherwise 0
        :keyword int newsitems: number of recent items appearing on the course page
        :keyword int startdate: timestamp when the course starts
        :keyword int enddate: timestamp when the course ends
        :keyword int numsections: (deprecated, use courseformatoptions) number of weeks/topics
        :keyword int maxbytes: largest size of file that can be uploaded into the course
        :keyword int showreports: are activity report shown (yes = 1, no = 0)
        :keyword int visible 1: available to students; 0: not available
        :keyword int hiddensections: (deprecated, use courseformatoptions) How the hidden sections in the course are displayed to students
        :keyword int groupmode: 0=no groups (no sub groups, one community), 1=separate groups (group members can only see members of their own group), 2=visible groups (groups work together, but can see other groups)
        :keyword int groupmodeforce: force course group mode onto all activities? (1: yes, 0: no)
        :keyword int defaultgroupingid: default grouping id (what does this do?)
        :keyword int timecreated: timestamp for course creation time
        :keyword int timemodified: timestamp for course modification time
        :keyword int enablecompletion: 1 - Enabled, control via completion and activity settings. 2 - Disabled, not shown in activity settings.
        :keyword int completionnotify: 1: yes 0: no
        :keyword string lang: forced course language
        :keyword string forcetheme: name of theme module to force for this course, or empty string for no forced theme.
        :keyword dict courseformatoptions: a list of format options (name/value pairs) for the course, in the form of dicts with 'name' and 'value' as keys. Names are alphanumeric, values raw strings (i.e. not formatting restriction on string contents)

        """
        params = self.config.request_params
        params.update({
            'wsfunction': 'core_course_get_courses',
            'ids': idlist
        })
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def get_courses_by_field(self, fieldname, value):
        """
        Fetch course data for specified courses.

        Returns {'courses': [...], 'warnings': [...]}

        Course data fetched:
        :keyword int id: course id
        :keyword string fullname: course full name
        :keyword string displayname: course display name
        :keyword string shortname: course short name
        :keyword int categoryid: id of category containing course
        :keyword int categoryname: name of category containing course
        :keyword string summary: course summary
        :keyword int summaryformat: format of summary (currently 1=FORMAT_HTML, 2=FORMAT_PLAIN, 3=FORMAT_WIKI, 4=FORMAT_MARKDOWN)

        Data also fetched if onlypublicdata is true:
        :keyword string idnumber: id number (for matching with external systems, never used within Moodle)
        :keyword string format: formatting plugin used for this course e.g. topics, social, site...
        :keyword int showgrades: 1 if grades are shown, otherwise 0
        :keyword int newsitems: number of recent items appearing on the course page
        :keyword int startdate: timestamp when the course starts
        :keyword int maxbytes: largest size of file that can be uploaded into the course
        :keyword int showreports: are activity report shown (yes = 1, no = 0)
        :keyword int visible 1: available to students; 0: not available
        :keyword int groupmode: 0=no groups (no sub groups, one community), 1=separate groups (group members can only see members of their own group), 2=visible groups (groups work together, but can see other groups)
        :keyword int groupmodeforce: force course group mode onto all activities? (1: yes, 0: no)
        :keyword int defaultgroupingid: default grouping id (what does this do?)
        :keyword int enablecompletion: 1 - Enabled, control via completion and activity settings. 2 - Disabled, not shown in activity settings.
        :keyword int completionnotify: 1: yes 0: no
        :keyword string lang: forced course language
        :keyword string theme: name of theme module to force for this course, or empty string for no forced theme.
        :keyword int sortorder: sort order into the category
        :keyword int marker: "Current course marker" - ???
        :keyword int legacyfiles: "If legacy files are enabled" - ???
        :keyword ??? calendartype: "Calendar type" -- PARAM_PLUGIN. ???
        :keyword int timecreated: timestamp for course creation time
        :keyword int timemodified: timestamp for course modification time
        :keyword int requested: "If it is a requested course" - ???
        :keyword int cacherev: "Cache revision number" - ???
        """
        params = self.config.request_params
        params.update({
            'wsfunction': 'core_course_get_courses_by_field',
            'field': fieldname,
            'value': value,
        })
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def delete(self, course_id):
        """
        Deletes a specified course

        Example Usage::

        >>> import muddle
        >>> muddle.course(10).delete()
        """
        params = {'wsfunction': 'core_course_delete_courses',
                  'courseids[0]': course_id}
        params.update(self.config.request_params)
        return requests.post(self.config.api_url, params=params, verify=False)

    def get_course_contents(self, course_id):
        """
        Returns entire contents of course page

        :returns: response object

        Example Usage::

        >>> import muddle
        >>> muddle.course(10).content()
        """
        params = self.config.request_params
        params.update({'wsfunction': 'core_course_get_contents',
                       'courseid': course_id})
        return requests.get(self.config.api_url, params=params, verify=False).json()

    def duplicate(self, course_id, fullname, shortname, categoryid,
                  visible=True, **kwargs):
        """
        Duplicates an existing course with options.
        Note: Can be very slow running.

        :param string fullname: The new course's full name
        :param string shortname: The new course's short name
        :param string categoryid: Category new course should be created under

        :keyword bool visible: Defaults to True. The new course's visiblity
        :keyword bool activities: (optional) Defaults to True. \
            Include course activites
        :keyword bool blocks: (optional) Defaults to True. \
            Include course blocks
        :keyword bool filters: (optional) Defaults to True. \
            Include course filters
        :keyword bool users: (optional) Defaults to False. Include users
        :keyword bool role_assignments: (optional) Defaults to False. \
            Include role assignments
        :keyword bool comments: (optional) Defaults to False. \
            Include user comments
        :keyword bool usercompletion: (optional) Defaults to False. \
            Include user course completion information
        :keyword bool logs: (optional) Defaults to False. Include course logs
        :keyword bool grade_histories: (optional) Defaults to False. \
            Include histories

        :returns: response object

        Example Usage::

        >>> import muddle
        >>> muddle.course(10).duplicate('new-fullname', 'new-shortname', 20)
        """

        # TODO
        # Ideally categoryid should be optional here and
        # should default to catid of course being duplicated.

        allowed_options = ['activities', 'blocks',
                           'filters', 'users',
                           'role_assignments', 'comments',
                           'usercompletion', 'logs',
                           'grade_histories']

        if valid_options(kwargs, allowed_options):
            option_params = {}
            for index, key in enumerate(kwargs):
                option_params.update(
                    {'options[' + str(index) + '][name]': key,
                     'options[' + str(index) + '][value]':
                        int(kwargs.get(key))})

            params = {'wsfunction': 'core_course_duplicate_course',
                      'courseid': course_id,
                      'fullname': fullname,
                      'shortname': shortname,
                      'categoryid': categoryid,
                      'visible': int(visible)}
            params.update(option_params)
            params.update(self.config.request_params)

            return requests.post(self.config.api_url, params=params, verify=False)

    def export_data(self, course_id, export_to, delete_content=False):
        """
        Export course data to another course.
        Does not include any user data.

        :param bool delete_content: (optional) Delete content \
            from source course.

        Example Usage::

        >>> import muddle
        >>> muddle.course(10).export_data(12)
        """
        params = {'wsfunction': 'core_course_import_course',
                  'importfrom': course_id,
                  'importto': export_to,
                  'deletecontent': int(delete_content)}
        params.update(self.config.request_params)

        return requests.post(self.config.api_url, params=params, verify=False)
