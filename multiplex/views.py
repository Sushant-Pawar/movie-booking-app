from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
def multiplexHome(request):
    response = {
        "message" : "Multplex Home"
    }
    return JsonResponse(response)
