

def valid_options(kwargs, allowed_options):
    """ Checks that kwargs are valid API options"""

    diff = set(kwargs) - set(allowed_options)
    if diff:
        print("Invalid option(s): ", ', '.join(diff))
        return False
    return True


