from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from . import utils


def login(request, success=True):
    """
    The first page of the app
    @param request: HttpRequest object
    @param success: Boolean to check if login had failed before
    @return: HttpResponse object
    """
    utils.session_funcs.clear_session(request)

    context = {"success": success, "error_msg": "Login failed, please try again"}
    return render(request, "mookit_downloader/login.html", context)


def login_action(request):
    """
    The page that executes login action of the app
    @param request: HttpRequest object
    @return: HttpResponse object
    """
    login_success = utils.helloiitk_login.login(
        request, request.POST["uname"], request.POST["password"]
    )

    if login_success:
        return HttpResponseRedirect(reverse("mookit_downloader:show_courses"))
    else:
        return HttpResponseRedirect(
            reverse("mookit_downloader:login_again", args=[int(login_success)])
        )


def show_courses(request):
    """
    The page that shows the courses
    @param request: HttpRequest object
    @return: HttpResponse object
    """
    context = {"course_codes": request.session[utils.COURSE_CODE_KEY]}
    return render(request, "mookit_downloader/courses.html", context)


def download_page(request, course_code):
    """
    The page showing download links to content
    @param request: HttpRequest object
    @param course_code: String containing course code passed in URL
    @return: HttpResponse object
    """
    context = {
        "course_code": course_code.lower(),
        "error": False,
        "error_message": "Some error occurred",
        "content": utils.get_course_content.get_content(request, course_code),
    }

    if context["content"] is False:
        context["error"] = True
    elif len(context["content"]) == 0:
        context["error"] = True
        context["error_message"] = "No content found"

    return render(request, "mookit_downloader/download.html", context)
