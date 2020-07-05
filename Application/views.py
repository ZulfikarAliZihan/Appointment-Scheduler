from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ApplicationForms
from .models import Application
# Create your views here.
def interview_list(request):
    context={'interviews':Application.objects.all()}
    return render(request,'Application/interview_list.html',context)

def interview_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=ApplicationForms()
        else:
            interview=Application.objects.get(pk=id)
            form = ApplicationForms(instance=interview)
        return render(request,"Application/interview_form.html",{'form':form})
    else:
        if id==0:
            form = ApplicationForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect("list/")
        else:
            interview = Application.objects.get(pk=id)
            form = ApplicationForms(request.POST,instance=interview)

            if form.is_valid():
                form.save()
            return redirect("../list/")

def interview_delete(request,id):
    interview = Application.objects.get(pk=id)
    interview.delete()
    return redirect("../list/")
