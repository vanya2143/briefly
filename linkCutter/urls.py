from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about/', views.about_page, name='about'),
    path('links/', views.UserLinks.as_view(), name='links-page'),
    path('link/<slug>', views.link_redirect, name='user-link')
]
