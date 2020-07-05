from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Session
from .forms import SessionForms
# Create your views here.
def session_list(request):
    context={'interviews':Session.objects.all()}
    return render(request,'Session/interview_list.html',context)

def session_form(request,id=0):
    if request.method == "GET":
        if id==0:
            form=SessionForms()
        else:
            interview=Session.objects.get(pk=id)
            form = SessionForms(instance=interview)
        return render(request,"Session/interview_form.html",{'form':form})
    else:
        if id==0:
            form = SessionForms(request.POST)
            if form.is_valid():
                form.save()
            return redirect("list/")
        else:
            interview = Session.objects.get(pk=id)
            form = SessionForms(request.POST,instance=interview)

            if form.is_valid():
                form.save()
            return redirect("../list/")

def session_delete(request,id):
    interview = Session.objects.get(pk=id)
    interview.delete()
    return redirect("../list/")