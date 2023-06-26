from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from register.models import Profile
from django.shortcuts import get_object_or_404

# Create your views here.

class ProfileList(ListView):
    model = Profile
    template_name = 'profiles/profiles_list.html'
    paginate_by = 2


# Detail view
class ProfileDetail(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'




    def get_object(self):
        print('Que me llega a qui_____   ',self.kwargs['username'])
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
        
