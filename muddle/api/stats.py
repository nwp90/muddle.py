from muddle.utils import valid_options

class API:
    """ Represents API endpoints for Moodle stats """

    def __init__(self, config):
        self.config = config

    def monthly_activity_by_shortname(self, course_shortname, time_start=None, time_end=None):
        """
        Fetch activity data for specified course.

        Returns array of monthly activity data per-role for the specified course.

        Activity data fetched:
        :keyword string uniqueid: an artificial unique id for the row
        :keyword int    courseid: course id
        :keyword string courseshortname: course short name
        :keyword int    roleid: role id for which this row contains activity
        :keyword string roleshortname: short name of role for which this row contains activity
        :keyword int    timeend: UNIX time before which accounted activity occurred
        :keyword int    activity_read: read activity by role during time period
        :keyword int    activity_write: write activity by role during time period
        """
        params = {
            'wsfunction': 'local_presentation_get_stats_activity_monthly_by_course',
            'course': course_shortname,
        }
        if time_start is not None:
            params['starttime'] = time_start
        if time_end is not None:
            params['endtime'] = time_end
        params.update(self.config.request_params)
        return self.config.session.get(self.config.api_url, params=params).json()

    def weekly_activity_by_shortname(self, course_shortname, time_start=None, time_end=None):
        """
        Fetch activity data for specified course.

        Returns array of weekly activity data per-role for the specified course.

        Activity data fetched:
        :keyword string uniqueid: an artificial unique id for the row
        :keyword int    courseid: course id
        :keyword string courseshortname: course short name
        :keyword int    roleid: role id for which this row contains activity
        :keyword string roleshortname: short name of role for which this row contains activity
        :keyword int    timeend: UNIX time before which accounted activity occurred
        :keyword int    activity_read: read activity by role during time period
        :keyword int    activity_write: write activity by role during time period
        """
        params = {
            'wsfunction': 'local_presentation_get_stats_activity_weekly_by_course',
            'course': course_shortname,
        }
        if time_start is not None:
            params['starttime'] = time_start
        if time_end is not None:
            params['endtime'] = time_end
        params.update(self.config.request_params)
        return self.config.session.get(self.config.api_url, params=params).json()

    def daily_activity_by_shortname(self, course_shortname, time_start=None, time_end=None):
        """
        Fetch activity data for specified course.

        Returns array of daily activity data per-role for the specified course.

        Activity data fetched:
        :keyword string uniqueid: an artificial unique id for the row
        :keyword int    courseid: course id
        :keyword string courseshortname: course short name
        :keyword int    roleid: role id for which this row contains activity
        :keyword string roleshortname: short name of role for which this row contains activity
        :keyword int    timeend: UNIX time before which accounted activity occurred
        :keyword int    activity_read: read activity by role during time period
        :keyword int    activity_write: write activity by role during time period
        """
        params = {
            'wsfunction': 'local_presentation_get_stats_activity_daily_by_course',
            'course': course_shortname,
        }
        if time_start is not None:
            params['starttime'] = time_start
        if time_end is not None:
            params['endtime'] = time_end
        params.update(self.config.request_params)
        return self.config.session.get(self.config.api_url, params=params).json()
