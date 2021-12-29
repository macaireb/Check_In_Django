from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    #path('', views.home, name="home"),
    path('', Home.as_view(), name="home"),
    path('resident/<int:pk>', ResidentDetail.as_view(), name="resident_detail"),
    path('resident/add_counselor', AddCounselor.as_view(), name="add_counselor"),
    path('resident/add_resident', AddResident.as_view(), name="add_resident"),
    #path('resident/add_punch', AddPunch.as_view(), name="add_punch"),
    path('resident/<int:pu>/add_punch', resident_punched, name="add_punch"),
    path('counselor/edit/<int:pk>', EditCounselor.as_view(), name="edit_counselor"),
    path('resident/edit/<int:pk>', EditResident.as_view(), name="edit_resident"),
    path('counselor/delete/<int:pk>', DeleteCounselor.as_view(), name="delete_counselor"),
    path('resident/delete/<int:pk>', DeleteResident.as_view(), name="delete_resident"),
    path('resident/punchlist', PunchList.as_view(), name="punch_list"),
    path('floor/<int:fl>/', FloorView, name='floor'),
]