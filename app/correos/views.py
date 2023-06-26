from django.shortcuts import render

from .models import Thread
from django.views.generic import TemplateView,DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404,JsonResponse
from .models import Thread,Message
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


@method_decorator(login_required,name='dispatch')
class ThreadList(TemplateView):
    def get_queryset(self):
        queryset = super(ThreadList,self).get_queryset()
        return queryset.filter(user=self.request.user)

    template_name='app_correos/thread_list.html'


    
@method_decorator(login_required,name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    def get_object(self):
        obj = super(ThreadDetail,self).get_object()
     
        if self.request.user not in obj.users.all():
            

            raise Http404
      
        return obj

# Funcion para crear mensajes 

def add_mensajes(request,pk):
    json_response={'created':False}

    # validamos si el usuario actual esta identificado
    if request.user.is_authenticated:
        content = request.GET.get('content',None)
        if content:

            thread = get_object_or_404(Thread,pk=pk)
            mensaje = Message.objects.create(user=request.user,content=content)
            thread.messages.add(mensaje)
            json_response['created']=True
        else:
            raise Http404("user is no authenticate")

    return JsonResponse(json_response)
