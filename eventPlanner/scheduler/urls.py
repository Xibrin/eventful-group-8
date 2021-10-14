from django.urls import path

from . import views

urlpatterns = [
    path('todo', views.TodoListView.as_view()),
]