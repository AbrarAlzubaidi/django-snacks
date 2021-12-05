from django.urls import path
from .views import AboutView , HomeView
urlpatterns = [
    path('home/', HomeView.as_view(), name = 'home'),
    path('about-us/', AboutView.as_view(), name = 'about-us'),
    ]