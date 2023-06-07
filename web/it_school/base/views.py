from django.views.generic import TemplateView
# Create your views here.
# in views este tot creierul aplicatiei.


class LandingPage(TemplateView):

    template_name = "base/index.html"
