from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm, EditProfileForm, PasswordChangingForm

# Create your views here.

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('home')

class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')


class LoginView(LoginRequiredMixin, View):
    form_class = AuthenticationForm
    template_name = "registration/login.html"
    success_url = reverse_lazy('home')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
