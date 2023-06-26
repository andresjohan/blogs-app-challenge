from .models import Thread , Message
from django.http import JsonResponse,HttpResponse

def python_javasCript(request,pk):

    json_response={'created':True}

    return JsonResponse(json_response)

