def register_user(email, password):
    pass

import re
def validate_email(email):
    return re.match(r'[^@]+@[^@]+\.[^@]+', email)
