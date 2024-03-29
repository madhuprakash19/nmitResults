from django.urls import path
from . import views
app_name = 'nmit'

urlpatterns = [
    path('sem5/',views.sem5,name='sem5'),
    path('sem2/',views.sem2,name='sem2'),
    path('sem7/',views.sem7,name='sem7'),
    path('sem3/',views.sem3,name='sem3'),
    path('sem1/',views.sem1,name='sem1'),
    path('sem6/',views.sem6,name='sem6'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('namewise',views.namewise,name='namewise'),
    path('result/<int:id>',views.result,name='result'),
    path('branchwise',views.branchwise,name='branchwise'),
    path('missingusn',views.missingusn,name='missing'),
    path('subject',views.subject,name='subject'),
    path('123hgds',views.test,name='test'),
]
