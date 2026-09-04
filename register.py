def register_user(email, password):
    pass

import re
def validate_email(email):
    return re.match(r'[^@]+@[^@]+\.[^@]+', email)

import hashlib
def hash_password(pwd):
    return hashlib.sha256(pwd.encode()).hexdigest()
