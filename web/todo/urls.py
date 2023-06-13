from django.urls import path
from todo.views import ListAll, ViewOne


urlpatterns = [
    path("", ListAll.as_view(), name="todo_list"),
    path("<int:pk>", ViewOne.as_view(), name="todo_one"),
]
