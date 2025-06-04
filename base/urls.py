from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing, name="home"),
    path('company/<slug:slug>/', views.company_page, name="company")
]