import requests
from bs4 import BeautifulSoup
from . import session_funcs
from . import constants
from .get_courses import get_courses


def login(request, uname, password):
    """
    Performs the login action
    @param request: HttpRequest object
    @param uname: username received from form
    @param password: password received from form
    @return: boolean indicating success of login
    """

    # Create requests session
    req_session = requests.Session()

    # Create the payload
    payload = {
        "name": uname,
        "pass": password,
        "form_id": "user_login_form",
        "op": "SIGN IN",
    }

    # Get BUILD ID
    res = req_session.get(constants.LOGIN_URL)
    soup = BeautifulSoup(res.content, "html.parser")
    build_ID = soup.find(attrs={"name": "form_build_id"}).get("value")
    payload["form_build_id"] = build_ID

    # Send POST request
    res = req_session.post(constants.LOGIN_URL, data=payload)

    # Check login success and store info in django's session
    session_funcs.init_session(request)
    try:
        request.session[constants.UID_KEY] = req_session.cookies["uid"]
        request.session[constants.TOKEN_KEY] = req_session.cookies["token"]

        get_courses(request, res.content)
        return True
    except Exception as e:
        print(e)
    finally:
        req_session.close()
    return False
