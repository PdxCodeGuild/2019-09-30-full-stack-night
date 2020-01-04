from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Todo

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos
    }

    return render(request, 'todos/list.html', context)

def details(request, id):
    todo = Todo.objects.get(id = id)

    return render(request, 'todos/detail.html', {"todo": todo})


def add_todo(request):
    if request.method == 'GET':
        return render(request, 'todos/add.html')
    elif request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        if (request.POST['status'] == 'False'):
            status = False
        else:
            status = True
        todo = Todo.objects.create(title = title, text = text, status = status)
        return redirect('list')


def remove_todo(request, id):
    todo = Todo.objects.get(id = id)
    todo.delete()
    return redirect('list')


def update_todo(request, id):
    todo = Todo.objects.get(id = id)
    print(request.POST['description'])
    return redirect('details', todo.id)


def update(request, id):
    todo = Todo.objects.get(id = id)
    if request.method == 'GET':
        return render(request, 'todos/update.html', {'todo': todo})
    elif request.method == 'POST':
        todo.title = request.POST['title']
        todo.text = request.POST['text']
        if (request.POST['status'] == 'False'):
            todo.status = False
        else:
            todo.status = True
        todo.save()
        return redirect('details', todo.id)

def mark_done(request, id):
    todo = Todo.objects.get(id = id)
    todo.status = True
    todo.save()

    return redirect('details', todo.id)