from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class LoginView(LoginRequiredMixin, View):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy('home')
