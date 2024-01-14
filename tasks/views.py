from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        # now the form will be filled with the data from request.POST
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    tasks = Task.objects.all()
    form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    # now prefil the form in accordance with the task object
    form = TaskForm(instance=task)

    if request.method == 'POST':
        # here a new form will not be created, instead the old form will be updated as the data from request.POST
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    context = {'item': item}
    return render(request, 'tasks/delete.html', context)
