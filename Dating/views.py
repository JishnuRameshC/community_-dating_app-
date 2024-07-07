from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from U_Auth.models import User

# Create your views here.
class HomePageView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'Dating/home.html'
    
    def get_queryset(self):
        return super(HomePageView, self).get_queryset().filter(is_staff=False, is_superuser=False).exclude(id=self.request.user.id)

