from django.contrib import admin
from dbApp1.models import student

# Register your models here.
class studentAdmin(admin.ModelAdmin):
    l=['name','number','marks']
admin.site.register(student,studentAdmin)
