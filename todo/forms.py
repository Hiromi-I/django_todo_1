from django import forms

from todo.models import Todo


class TodoCreateForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title',)
