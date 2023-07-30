from django.shortcuts import render

# Create your views here.

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!"})
    return Response({"message": "Hello, world!"})
    