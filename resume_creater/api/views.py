from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api(request):
    data = {
        "message": "hello world"
    }
    return JsonResponse(data)