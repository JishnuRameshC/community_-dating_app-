from django.urls import path
from .views import *


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', signout, name='logout'),

    path('register/', RegisterPage1View.as_view(), name='register'),
    path('register2/',RegisterPage2View.as_view(),name='register2'),
    path('register3/',RegisterPage3View.as_view(),name='register3'),

    path('profile/', ProfileView.as_view(), name='profile'),

    path('address/', AddressListView.as_view(), name='address_list'),
    path('address/create/', AddressCreateView.as_view(), name='address_create'),
    path('address/update/<int:id>/', AddressUpdateView.as_view(), name='address_update'),
    path('address/delete/<int:id>/', AddressDeleteView.as_view(), name='address_delete'),
]