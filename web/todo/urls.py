from django.urls import path
from todo.views import ListAll, ViewOne


urlspatters = [
    path("todo/", ListAll.as_view(), name="todo_list"),
    path("todo/<int:pk>", ViewOne.as_view(), name="todo_one"),
]
