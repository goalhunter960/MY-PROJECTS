from django.urls import path
from management import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact/', views.contact, name='contact'),
]
