from django.shortcuts import render
from . import forms
from formApp.models import Feedback
# Create your views here.
def FeedbackView(request):
    form=forms.Feedbackform
    if request.method=='POST':
        form=forms.Feedbackform(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'feedbackform.html',{'form':form})

def ShowView(request):
    s=Feedback.objects.all()
    return render(request,'show.html',{'s':s})
