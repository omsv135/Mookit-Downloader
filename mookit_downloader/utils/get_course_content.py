import requests
from . import session_funcs
from . import constants


def get_content(request, course_code):
    """
    Retrieves the course content from the Mookit API
    @param request: HttpRequest object
    @param course_code: string containing the course code
    @return: list of dictionaries having course content or boolean False if retrieval failed
    """
    try:
        URL = constants.API_URL + course_code.lower() + "/lectures/summary"
        headers = {
            "uid": request.session[constants.UID_KEY],
            "token": request.session[constants.TOKEN_KEY],
        }

        json_response = requests.get(URL, headers=headers).json()
        entries = []
        for entry in json_response:
            data = {
                "week": entry["week"],
                "topic": entry["topic"],
                "title": entry["title"],
                "vidURL": entry["videosUploaded"],
                "resources": entry["resources"],
            }
            entries.append(data)
        return entries
    except Exception as e:
        print("The following exception occurred:", e, sep="\n")
        session_funcs.clear_session(request)
        return False
