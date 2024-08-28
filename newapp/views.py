from django.shortcuts import render, redirect
from newapp.models import *
from django.http import HttpResponse

''' Student Model '''
def table(request):
    tasks = TODO.objects.all()
    context = {
        'tasks': tasks,
        'total_task': tasks.count(),
        'completed_task': tasks.filter(status=True).count(),
        'pending_task': tasks.filter(status=False).count(),
    }
    return render (request, 'table.html', context)


def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        TODO.objects.create(title=title, description=description)
        return redirect('table')
    
    return render(request, 'create_task.html')


def task_pending(request, pk):
    tasks = TODO.objects.get(pk=pk)
    tasks.status = False
    tasks.save()
    
    return redirect('table')


def task_complete(request, pk):
    tasks = TODO.objects.get(pk=pk)
    tasks.status = True
    tasks.save()
    
    return redirect('table')


def update_task(request, pk):
    task = TODO.objects.get(pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        task.title = title
        task.description = description

        task.save()

        return redirect('table')

    return render(request, 'update.html', {'task':task})


def delete_task(request, pk):
    tasks = TODO.objects.get(pk=pk)

    tasks.delete()

    return redirect('table')

''' Employee MODEL '''

def employee_table(request):
    employees = Employee.objects.all()
    return render(request, 'employee/table.html', {'employees':employees})

def employee_create(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        salary = request.POST.get('salary')
        department = request.POST.get('department')

        Employee.objects.create(name=name, age=age, address=address, gender=gender, salary=salary, department=department )
        return redirect('employee_table')
    
    return render(request, 'employee/create.html')

