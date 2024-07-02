from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import View,CreateView
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView

from .forms import LoginForm,UserForm,EmployeeEmployerForm,Address,AddressUpsertForm

class Demo(TemplateView):
    template_name = 'U_Auth/signup.html'


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'U_Auth/login.html', {'form': form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # return HttpResponse(f'Login Successful username: {username}')
                return redirect('/')

        return render(request, 'U_Auth/login.html', {'form': form})
    

class RegisterPage1View(CreateView):
    form_class = UserForm
    success_url = reverse_lazy("register2")
    template_name = "U_Auth/register_step_1.html"


class RegisterPage2View(CreateView):
    form_class = EmployeeEmployerForm
    success_url = reverse_lazy("register3")
    template_name = "U_Auth/register_step_2.html"

class RegisterPage3View(TemplateView):
    template_name = "U_Auth/register_step_3.html"


def signout(request):
    logout(request)
    return redirect('/')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Dating/profile_view.html'


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    template_name = 'Dating/address_list.html'
    # queryset = Address.objects.filter(user=1)

    def get_queryset(self):
        # return Address.objects.filter(user=self.request.user)
        return super(AddressListView, self).get_queryset().filter(user=self.request.user)


class AddressCreateView(LoginRequiredMixin, CreateView):
    model = Address
    form_class = AddressUpsertForm
    template_name = 'Dating/address_upsert.html'
    success_url = reverse_lazy('address_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddressCreateView, self).form_valid(form)
    

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    model = Address
    form_class = AddressUpsertForm
    template_name = 'Dating/address_upsert.html'
    pk_url_kwarg = 'id'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class AddressDeleteView(LoginRequiredMixin, View):
    def get(self, request, id):
        address = get_object_or_404(Address, id=id, user=self.request.user)
        address.delete()
        return redirect('address_list')

