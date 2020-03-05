from django.shortcuts import render

from todo.models import Todo


def todo_list(request):
    todo_list = Todo.objects.all()
    return render(request, 'todo/list.html', {'todo_list': todo_list})
