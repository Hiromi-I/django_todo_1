from django.test import TestCase
from django.urls import reverse

from todo.models import Todo


class TestTodoList(TestCase):
    def test_get(self):
        response = self.client.get(reverse('todo:todo_list'))
        self.assertTemplateUsed(response, 'todo/list.html')

class TestTodoDelete(TestCase):
    def test_delete(self):
        Todo.objects.create(id=1, title="todo1")
        self.assertEqual(len(Todo.objects.all()), 1)

        response = self.client.post(
            reverse('todo:todo_delete', args=(1,)))

        self.assertEqual(len(Todo.objects.all()), 0)
        self.assertRedirects(response, reverse('todo:todo_list'))
