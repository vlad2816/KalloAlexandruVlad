from django.views.generic import TemplateView

# Create your views here.
# M V C
# M T V -> django

# Class-based views

class LandingPage(TemplateView):

    template_name = "base/landing.html"
