from django.urls import path
from .views import ThreadList,ThreadDetail,add_mensajes
from.views2 import python_javasCript



urlpatterns = [ path('',ThreadList.as_view(),name='lista'),
                path('thread/<int:pk>/',ThreadDetail.as_view(),name='detailCorreo'),
                
                path('thread/<int:pk>/add/',add_mensajes,name='add'),
                path('tree/<int:pk>/agregar/',python_javasCript,name='agregar')
              ]