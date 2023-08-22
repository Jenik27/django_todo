from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'tasks': tasks, 'form': form}
    return render(request, 'home.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('home')

def updateTask(request, pk):
    item = Task.objects.get(id=pk)
    form = TaskForm(instance=item)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'update.html', context)
