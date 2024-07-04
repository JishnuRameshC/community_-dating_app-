from django.urls import path
from .views import *

appname = 'dating'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
]
