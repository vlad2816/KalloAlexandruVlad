from django.urls import path
from py_math.views import FunView, AllHistory

urlpatterns = [
    path("fun", FunView.as_view(), name="math-fun"),
    path("fun/history", AllHistory.as_view(), name="math-history")

]
