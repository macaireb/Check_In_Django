from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Resident, Counselor, Punch
from .forms import CounselorForm, ResidentForm, EditCounselorForm, EditResidentForm, PunchForm

# Create your views here.

#def home(request):
#   return render(request, 'resident_punch/home.html', {})

class Home(ListView):
        model = Resident
        template_name = "resident_punch/home.html"
        #ordering = ['-id']

class ResidentDetail(DetailView):
        model = Resident
        template_name = "resident_punch/resident_punch_detail.html"

class PunchList(ListView):
        model = Punch
        template_name = "resident_punch/punch_list.html"


class AddCounselor(CreateView):
        model = Counselor
        form_class = CounselorForm
        template_name = "resident_punch/add_counselor.html"
        # fields = {'first_name', 'last_name'}


class AddResident(CreateView):
        model = Resident
        form_class = ResidentForm
        template_name = "resident_punch/add_resident.html"
        # fields = {'first_name', 'last_name', 'counselor'}


class AddPunch(CreateView):
        model = Punch
        form_class = PunchForm
        template_name = "resident_punch/punch_clock.html"


class EditCounselor(UpdateView):
        model = Counselor
        form_class = EditCounselorForm
        template_name = "resident_punch/edit_counselor.html"
        #fields = {'first_name', 'last_name'}


class EditResident(UpdateView):
        model = Resident
        form_class = EditResidentForm
        template_name = "resident_punch/edit_resident.html"
        #fields = {'first_name', 'last_name', 'counselor'}


class DeleteCounselor(DeleteView):
        model = Counselor
        template_name = "resident_punch/delete_counselor.html"
        success_url = reverse_lazy('home')


class DeleteResident(DeleteView):
        model = Resident
        template_name = "resident_punch/delete_resident.html"
        success_url = reverse_lazy('home')
