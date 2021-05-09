from django.shortcuts import render
from dbApp1.models import student

# Create your views here.
def view(request):
    e=student.objects.all()
    d={"emp":e}
    return render(request,"dbApp1/1.html",d)