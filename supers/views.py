from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SuperSerializer
from .models import Super

# Create your views here.
@api_view(['GET'])
def supers_list(request):

    return Response('')


@api_view(['GET'])
def supers_detail(request):

    return Response('')

