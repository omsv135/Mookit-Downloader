from django.urls import path

from . import views

app_name = "mookit_downloader"
urlpatterns = [
    path("", views.login, name="login"),
    path("login/", views.login_action, name="login_action"),
    path("login/<int:success>/", views.login, name="login_again"),
    path("courses/", views.show_courses, name="show_courses"),
    path("courses/<str:course_code>/", views.download_page, name="download_page"),
]
