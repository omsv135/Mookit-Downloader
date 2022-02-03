from bs4 import BeautifulSoup

COURSES_DIV_ID = "block-views-block-courses-block-1"


def get_course_from_link(link):
    """
    Returns the course code obtained by getting the string after last slash ('/') in link passed.
    @param link: String having link
    @return: String having course code obtained from link
    """
    course = ""
    for idx in range(len(link) - 1, 0, -1):
        if link[idx] == "/":
            break
        course += link[idx]
    return course[::-1]


def get_courses(request, html):
    """
    The course codes and course names are added to the session data.
    @param request: HttpRequest object
    @param html: The HTML content obtained after logging in
    @return: None
    """
    soup = BeautifulSoup(html, "html.parser")

    # Find the <a> tag which contain link to courses
    courses_div = soup.find(id=COURSES_DIV_ID)
    link_tags = courses_div.find_all("a")

    # Obtain the links from <a> tags
    links = [tag["href"] for tag in link_tags]

    # Obtain the course codes from links
    courses = []
    for link in links:
        courses.append(get_course_from_link(link))

    request.session["course_codes"] = courses
