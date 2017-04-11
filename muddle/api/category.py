import requests
from muddle.utils import valid_options


class API:
    """ Represents API endpoints for Moodle Course Categories """

    def __init__(self, config):
        self.config = config

    def details(self, category_id):
        """
        Returns details for given category

        :returns: category response object

        Example Usage::

        >>> import muddle
        >>> muddle.category(10).details()
        """
        params = {'wsfunction': 'core_course_get_categories',
                  'criteria[0][key]': 'id',
                  'criteria[0][value]': category_id}

        params.update(self.config.request_params)

        return requests.post(self.config.api_url, params=params, verify=False)

    def create(self, category_name, **kwargs):
        """

        Create a new category

        :param string name: new category name
        :param int parent: (optional) Defaults to 0, root category. \
            The parent category id inside which the new \
            category will be created
        :param string description: (optional) The new category description
        :param int descriptionformat: (optional) Defaults to 1 \
            description format (1 = HTML,
                                0 = MOODLE,
                                2 = PLAIN,
                                4 = MARKDOWN)
        :param string theme: (optional) The new category theme

        Example Usage::

        >>> import muddle
        >>> muddle.category().create('category name')
        """
        allowed_options = ['parent',
                           'description',
                           'descriptionformat',
                           'theme']

        if valid_options(kwargs, allowed_options):
            option_params = {}
            for key in kwargs:
                option_params.update(
                    {'categories[0][' + key + ']': str(kwargs.get(key))})
            params = {'wsfunction': 'core_course_create_categories',
                      'categories[0][name]': category_name,
                      }
            params.update(option_params)
            params.update(self.config.request_params)

            return requests.post(self.config.api_url, params=params, verify=False)

    def delete(self, category_id, new_parent=None, recursive=False):
        """
        Deletes a category. Optionally moves content to new category.
        Note: If category is in root, new_parent must be specified.

        :param int new_parent: (optional) Category ID of new parent
        :param bool recursive: recursively delete contents inside this category

        Example Usage::

        >>> import muddle
        >>> muddle.category(10).delete()
        """

        params = {'wsfunction': 'core_course_delete_categories',
                  'categories[0][id]': category_id,
                  'categories[0][recursive]': int(recursive)}
        if new_parent:
            params.update({'categories[0][newparent]': new_parent})
        params.update(self.config.request_params)

        return requests.post(self.config.api_url, params=params, verify=False)

    def update(self, category_id, **kwargs):
        """
        Update categories

        :param string name: (optional) Name
        :param string idnumber: (optional) Id number
        :param int parent: (optional) Parent category id
        :param string description: (optional) Description
        :param int description-format: Defaults to 1 \
            (1 = HTML, 0 = MOODLE, 2 = PLAIN or 4 = MARKDOWN)
        :param string theme: (optional) Theme

        Example Usage::

        >>> import muddle
        >>> muddle.category(10).update(name='new name')
        """

        allowed_options = ['name', 'idnumber', 'parent',
                           'description', 'descriptionformat',
                           'theme']

        if valid_options(kwargs, allowed_options):
            option_params = {}
            for key in kwargs:
                option_params.update(
                    {'categories[0][' + key + ']': str(kwargs.get(key))})

            params = {'wsfunction': 'core_course_update_categories',
                      'categories[0][id]': category_id}
            params.update(option_params)
            params.update(self.config.request_params)

            return requests.post(self.config.api_url, params=params, verify=False)
