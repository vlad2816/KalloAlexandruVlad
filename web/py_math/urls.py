from django.urls import path
from py_math.views import FunView

urlspatterns = [
    path("fun", FunView.as_view(), name="math-fun")
]
