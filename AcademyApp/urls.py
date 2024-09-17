from django.contrib import admin
from django.urls import path
from AcademyApp import views

urlpatterns = [
    path('',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('dashboard',views.home,name='dashboard'),
    path('addStd',views.addStd,name='addStd'),
    path('payment',views.payment,name='payment'),
    path('details',views.details,name='details'),
    path('payDetails',views.payDetails,name='payDetails'),
]
