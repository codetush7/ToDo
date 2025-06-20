from django.shortcuts import render
from django.shortcuts import redirect
from .models import Task
from django.views.generic import ListView


class TaskListView(ListView):
    model= Task
    template_name = 'myapp/index.html'
    context_object_name='task_list'


 

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')
        task = Task(name=name,priority=priority)
        task.save()
        return redirect('/') 
    task_list = Task.objects.all()
    return render(request,'myapp/index.html',{'task_list': task_list})


def delete(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method=="POST":
        action = request.POST.get("action")
        if action == "yes":
            task.delete()
            return redirect('/')
        else:
            return redirect('/')
    return render(request,'myapp/delete.html',{'task':task})

def update(request,taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.name = request.POST.get('name')
        task.priority = request.POST.get('priority')
        task.date = request.POST.get('date') 
        task.save()
        return redirect('/')

    return render(request,'myapp/update.html',{'task':task})


