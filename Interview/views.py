from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import InterviewForms
from .models import Interview

# Create your views here.
def interview_list(request):
    context={'interviews':Interview.objects.all()}
    return render(request,'Interview/interview_list.html',context)

def interview_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=InterviewForms()
        else:
            interview=Interview.objects.get(pk=id)
            form = InterviewForms(instance=interview)
        return render(request,"Interview/interview_form.html",{'form':form})
    else:
        if id==0:
            form = InterviewForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect("list/")
        else:
            interview = Interview.objects.get(pk=id)
            form = InterviewForms(request.POST,instance=interview)

            if form.is_valid():
                form.save()
            return redirect("../list/")

def interview_delete(request,id):
    interview = Interview.objects.get(pk=id)
    interview.delete()
    return redirect("../list/")
