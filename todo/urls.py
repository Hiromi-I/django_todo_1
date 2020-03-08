from django.urls import path

from todo import views


app_name = 'todo'

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('create/', views.todo_create, name='todo_create'),
    path('edit/<int:todo_id>/', views.todo_edit, name='todo_edit'),
]
