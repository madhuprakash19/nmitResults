from django.urls import path
from . import views
app_name = 'nmit'

urlpatterns = [
    path('home/',views.home,name='home'),
]
