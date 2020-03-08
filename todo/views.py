from django.shortcuts import render, redirect, get_object_or_404

from todo.models import Todo
from todo.forms import TodoCreateForm, TodoEditForm


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


def todo_edit(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'GET':
        form = TodoEditForm(instance=todo)
        return render(request, 'todo/edit.html', {'form': form})
    else:
        form = TodoEditForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo:todo_list')
        else:
            return render(request, 'todo/edit.html', {'form': form})
