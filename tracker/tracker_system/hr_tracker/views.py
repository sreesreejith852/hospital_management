from django.shortcuts import render
from .models import Task


def create_task(request):
    print("aaaaaaaaaa")
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')

        task = Task(
            title = title,
            description = description,
            # completed = True

        )
        task.save()
    return render(request,'create.html')

def list_task(request):
    print("listtttttttttttttttttttttttttttt")
    task_list=Task.objects.all()
    print(task_list)
    return render(request,'list.html',{'tasks':task_list})
    

