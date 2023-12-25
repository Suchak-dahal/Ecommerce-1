from django.urls import include, path

from .views import *
urlpatterns = [
    path('', HomeView.as_view(), name='home')
]

