from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from U_Auth.models import User

# Create your views here.
class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    template_name = 'Dating/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_staff=False, is_superuser=False, is_active=True)
        return context
    