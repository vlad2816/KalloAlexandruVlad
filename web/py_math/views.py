from django.shortcuts import render
from django.views.generic import View


class FunView(View):

    def get(self, request):
        return "Hello world"
