from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm

# Create your views here.

def home(request):
    tasks=Task.objects.all()
    form=TaskForm

    if request.method=="POST":
        Task.objects.create(
            title=request.POST.get("title"),
        )
        return redirect("/")

    context={
        "page_title":"Tasks",
        "tasks":tasks,
        "form":form
    }
    return render(request,"home.html",context)