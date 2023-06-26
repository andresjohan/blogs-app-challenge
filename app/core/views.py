from typing import Any
from django import http
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render


# prueba
class HomePageView(TemplateView):

    template_name = "core/home.html"

 
    def get(self,request):
        return render(request,self.template_name,{'title':'Blogs y Registros '})




class samplePageView(TemplateView):
    template_name = "core/sample.html"


