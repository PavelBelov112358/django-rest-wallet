from django.urls import path

from .views import *


urlpatterns = [
    path('wallet/', TestView.as_view())
]
