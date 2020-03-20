from django.test import TestCase
from django.urls import reverse


class TestTodoList(TestCase):
    def test_get(self):
        response = self.client.get(reverse('todo:todo_list'))
        self.assertTemplateUsed(response, 'todo/list.html')
