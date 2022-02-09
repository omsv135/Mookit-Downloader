import requests
from . import session_funcs
from . import constants


def group_the_weeks(entries):
    """
    Groups the content of same week into a list, returning a 2-D array.
    @param entries: Array of data entries
    @return: 2-D array
    """
    week_names = []
    for entry in entries:
        if entry["week"] not in week_names:
            week_names.append(entry["week"])

    segregated_entries = []
    for week_name in week_names:
        same_week = []
        for entry in entries:
            if week_name == entry["week"]:
                same_week.append(entry)
        segregated_entries.append(same_week)

    return segregated_entries


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
        return group_the_weeks(entries)
    except Exception as e:
        print("The following exception occurred:", e, sep="\n")
        session_funcs.clear_session(request)
        return False
