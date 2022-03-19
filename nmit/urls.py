from django.urls import path
from . import views
app_name = 'nmit'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('namewise',views.namewise,name='namewise'),
    path('result/<int:id>',views.result,name='result')
]
