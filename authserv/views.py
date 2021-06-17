from django.http import response
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(['GET'])
def authHome(request):
    response = {
        "message": "Auth Home" 
    }
    return Response(response)


