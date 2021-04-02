from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from .models import *
from .serializers import *


class TestView(CreateModelMixin, ListModelMixin, RetrieveAPIView, APIView):
    pass


class Test1View(ViewSet):
    pass
