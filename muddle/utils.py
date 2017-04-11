

def valid_options(kwargs, allowed_options):
    """ Checks that kwargs are valid API options"""

    diff = set(kwargs) - set(allowed_options)
    if diff:
        print("Invalid option(s): ", ', '.join(diff))
        return False
    return True


def clean_username(value):
    # Moodle checks username params are valid by "cleaning" it
    # and then comparing to original. If original differs from
    # cleaned value, it barfs. So we need to clean in approx the
    # same manner before submitting request, to cater for
    # carelessness in spreadsheet preparation & trying group names
    # as usernames etc.

    # "fix_utf8"
    # "trim"
    # downcase
    # if empty($CFG->extendedusernamechars), restrict to [-\.@_a-z0-9]

    # we'll trust valid UTF8; we can accept an error if it's not
    # we'll assume extendedusernamechars is not turned on.
    # Because then all we have to do is:
    from re import sub
    return sub(r'[^-\.@_a-z0-9]', '', value.lower())
    
