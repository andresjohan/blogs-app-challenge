from django.test import TestCase
from .models import Thread,Message
from django.contrib.auth.models import User
# Create your tests here.

class ThreadTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('juan',None,'test1234')
        self.user2 = User.objects.create_user('ramon',None,'test1234')
        
        
        self.thread = Thread.objects.create()
    
    def  test_create_users(self):
        self.thread.users.add(self.user1,self.user2)
        
        self.assertEqual(len(self.thread.messages.all()),0)


    
    def test_obtener_Thread_by_user(self):
        # hilo creado para dos usuarios especificos 
        self.thread.users.add(self.user1,self.user2)

        threads = Thread.objects.filter(users=self.user1).filter(users=self.user2)

        self.assertEqual(self.thread,threads[0])

  


    

        
    def test_add_message_from_user_not_in_thread(self):
        self.thread.users.add(self.user1,self.user2)
        
        print("user1",self.user1)
        print("user2",self.user2)

        message1 = Message.objects.create(user=self.user1,content='hola buenas')
        message2 = Message.objects.create(user=self.user2,content='hola toby')

 
        self.thread.messages.add(message1,message2)

        self.assertEqual(len(self.thread.messages.all()),2)

