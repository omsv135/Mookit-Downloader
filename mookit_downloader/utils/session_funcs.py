def init_session(request):
    # Sets expiry of session data at browser close
    request.session.set_expiry(0)


def clear_session(request):
    # Removes the session data
    request.session.flush()
