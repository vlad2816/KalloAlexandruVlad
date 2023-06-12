from django.views.generic import ListView, DetailView
from todo.models import Todo
# Create your views here.


class ListAll(ListView):
    template_name = "todo/list.html"
    model = Todo


class ViewOne(DetailView):
    template_name = "todo\detail.html"
    model = Todo
