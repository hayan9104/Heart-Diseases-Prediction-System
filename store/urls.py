from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('firstpg/', views.firstpg, name='firstpg'),
    path('firstpg/adminpage', views.adminpage, name='adminpage'),
    path('firstpg/user_adminpg/', views.user_adminpg, name='user_adminpg'),
    path("userpg/", views.userpg, name="userpg"),
    path("user_page/", views.user_page, name="user_page"),
    path('user_adminpg/', views.user_adminpg, name='user_adminpg'),
    path('hypertension/', views.hypertension, name='hypertension'),
    path('last_consultation/', views.last_consultation, name='last_consultation'),
    path('next_appointment/', views.next_appointment, name='next_appointment'),
    path('home/', views.home, name='home'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('history_list/', views.history_list, name='history_list'),
    path('patient/<str:case_no>/', views.patient_detail, name='patient_detail'),
    path('patient/<str:case_no>/', views.user_patientdetail, name='user_patientdetail'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('predict/', views.predict, name='predict'),
    path('fectors/', views.fectors, name='fectors'),
    path('authenticate/', views.authenticate, name='authenticate'),
    path('update_password/', views.update_password, name='update_password'),
    path('last-consultation/', views.last_consultation, name='last-consultation'),
    path('heart_arrhythmias/', views.heart_arrhythmias, name='heart_arrhythmias'),
    path('cad/', views.cad, name='cad'),
    path('mayocardial/', views.mayocardial, name='mayocardial'),
]


