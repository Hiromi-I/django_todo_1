from django.shortcuts import render, redirect

from todo.models import Todo
from todo.forms import TodoCreateForm


def todo_list(request):
    todo_list = Todo.objects.all()
    return render(request, 'todo/list.html', {'todo_list': todo_list})


def todo_create(request):
    if request.method == 'GET':
        form = TodoCreateForm()
        return render(request, 'todo/create.html', {'form': form})
    else:
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
        else:
            return render(request, 'todo/create.html', {'form': form})
