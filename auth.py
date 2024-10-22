def login_user(username, password):
    # This is a placeholder. In a real application, you would check against a database
    # and use proper password hashing.
    if username == "admin" and password == "password":
        return True
    return False