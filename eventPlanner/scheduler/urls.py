from django.urls import path

from . import views

urlpatterns = [
    path('', views.user_view, name="user"),

    # User authentication URLs
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('register', views.register_view, name="register"),

    # Events API URL
    path('events', views.events_view, name="events"),
    path('schedule', views.schedule_view, name="schedule")
]