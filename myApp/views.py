from django.shortcuts import render
from myApp.models import employee
# Create your views here.
def view1(request):
    e = employee.objects.all()
    d = {'emp': e}
    return render(request,'myApp/1.html',d)