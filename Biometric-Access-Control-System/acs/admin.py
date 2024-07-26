from django.contrib import admin

from .models import Student, Tracker, MyModel

# Register your models here.
admin.site.register(MyModel)
admin.site.register(Student)
admin.site.register(Tracker)

