


from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreationWithEmail ,EmailForm
from django.views.generic import CreateView
from django.views.generic import TemplateView,UpdateView
from django.urls import reverse_lazy
from django import forms
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm


# Create your views here.

class SingUpView(CreateView):

    form_class = UserCreationWithEmail

    # # me redirecciona a una url

    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register'
    
    #modificacion Estetica Formulario De registro
    def get_form(self, form_class=None):
        form = super(SingUpView,self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Nombre De  Usuario'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Direccion Email'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Password1'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Password2'})
        return form


@method_decorator(login_required,name='dispatch')
class ProfileUdateModel(UpdateView):

    form_class = ProfileForm
    template_name = 'registration/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')+'?ok'


    
    def get_object(self) :

        profile,created = Profile.objects.get_or_create(user=self.request.user)
        return profile
    


@method_decorator(login_required,name='dispatch')
class EmailUpdate(UpdateView):

    form_class = EmailForm
    template_name = 'registration/profile_email_form.html'

    # Dejamos esta ruta para que me muestre como quedo el perfil despues de update 
    success_url = reverse_lazy('profile')


    # metodo para recuperar el usuario

    def get_object(self) :

        return self.request.user

    # metodo de sobreescritura  para widget o imagen del campo
    def get_form(self,form_class=None):

        form = super(EmailUpdate,self).get_form()
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'EMAIL'})
        return form










