from django.contrib import admin
from .models import student,course,type

# Register your models here.
admin.site.register(student)
admin.site.register(course)
admin.site.register(type)