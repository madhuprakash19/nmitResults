from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.student)
admin.site.register(models.subjects)
admin.site.register(models.gpa)
admin.site.register(models.marks)
