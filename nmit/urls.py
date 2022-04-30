from django.urls import path
from . import views
app_name = 'nmit'

urlpatterns = [
    path('sem5/',views.sem5,name='sem5'),
    path('sem7/',views.sem7,name='sem7'),
    path('sem3/',views.sem3,name='sem3'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('namewise',views.namewise,name='namewise'),
    path('result/<int:id>',views.result,name='result'),
    path('branchwise',views.branchwise,name='branchwise'),
    path('missingusn',views.missingusn,name='missing'),
]
