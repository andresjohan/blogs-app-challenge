from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .forms import FormModel


#mixin de autentificacion
class StaffRequiredMixin(object):

    # verificacion de autentificacion 
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required,name='dispatch')
class ArticleListView(ListView):
     model = Page

@method_decorator(staff_member_required,name='dispatch')
class ArticleDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required,name='dispatch')
class AuthorCreate(CreateView):
    model = Page
    form_class = FormModel

    def get_success_url(self):
        return reverse('pages')
    

    def dispatch(self, request, *args,**kwargs):
        print('El Usuario Es _________   ',request.user)

        if not request.user.is_staff:
            return render(reverse_lazy('admin:login'))
        return super(AuthorCreate,self).dispatch(request, *args, **kwargs)
    




    
@method_decorator(staff_member_required,name='dispatch')
class PageUpdate(UpdateView):
    model = Page
    fields = ['title','content','order']


    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id]) + '?ok' 
    



@method_decorator(staff_member_required,name='dispatch')
class PageDelete(DeleteView):
    model = Page

    #Redireccionamos a la lista con todas las paginas 
    success_url = reverse_lazy('pages')
    
class CreatedView2(CreateView):
    model = Page
    fields = ['title','contente','order']
    template_name_suffix = '_update_form'

class UpdateView2(UpdateView):
    model = Page
    fields = ['title','content','order']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('update',args=[self.object.id]) 





    

    