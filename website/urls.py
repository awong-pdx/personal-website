from django.urls import path
from website import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("previous-work/", views.previous_work, name="previous-work"),
    path("projects/", views.projects, name="projects"),
]
