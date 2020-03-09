
from django.shortcuts import render
from . import forms
from hrApp.forms import EmployeeForm

# Create your views here.
def EmployeeView(request):
    form=forms.EmployeeForm()
    if request.method=='POST':
        form=forms.EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    return render(request,'employee.html',{'form':form})
# Create your views here.
