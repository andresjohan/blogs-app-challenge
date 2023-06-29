from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class UserCreationWithEmail(UserCreationForm):
    email = forms.EmailField(required=True,help_text='Requiere 254 debe ser valido')


    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    


    def clean_email(self):

        # Entramos a la variable donde se almacena el email y atrapamos el valor
        email = self.cleaned_data.get('email')

        #Buscamos el email
        if User.objects.filter(email=email).exists():

            #Devolvemos mensaje de herror 
            raise forms.ValidationError('El email ya esta Rejistrado')
        return email
    
    from django.template import Library


   

class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio':forms.Textarea(attrs={'class':'form-control mt-3','rows':3,'placeholder':'Biografia'}),
            'bio':forms.URLInput(attrs={'class':'form-control mt-3','rows':3,'placeholder':'Enlace'})
        }


# logica
class EmailForm(forms.ModelForm):

    # creamos campo para email
    email = forms.EmailField(required=True,help_text='Requiere 254 debe ser valido')

    # creamos clase meta para personalizar un campo o modelos
    class Meta:
        # pasamos el modelos que queremos personalizar
        model = User
        
      
        fields = ['email']

        # validacion de campo email
        def clean_email(self):


            email = self.cleaned_data.get('email')

            if 'email' in self.changed_data:

                #Buscamos el email si existe
                if User.objects.filter(email=email).exists():

                    #Devolvemos mensaje de herror 
                    raise forms.ValidationError('El email ya esta Rejistrado')
            
            return email
