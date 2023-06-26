from django.db import models
from django.db.models.signals import m2m_changed

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class ThreadManager(models.Manager):

    def find(self,user1,user2):

        # me filtra y me trae estos 2 usuarios 
       
        queryset=self.filter(users=user1).filter(users=user2)
        if len(queryset) > 0:
            
            # returna un query set osea registro
            return queryset[0]
        
        return None


    def find_or_create(self,user1,user2):
        thread = self.find(user1,user2)

        if thread is None:

            # lo creamos vacio
            thread = Thread.objects.create()

            # luego agregamos los usuarios
            thread.users.add(user1,user2)

        return thread
    
# >>> from correos.models import Thread
# >>> from correos.models import Message
# >>> johan = User.objects.get(username='johan')
# >>> natalia = User.objects.get(username='natalia')
# >>> thread = Thread.objects.find_or_create(johan,natalia)




# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Thread(models.Model):
    users = models.ManyToManyField(User,related_name='threads')
    messages = models.ManyToManyField(Message)

    objects = ThreadManager()






