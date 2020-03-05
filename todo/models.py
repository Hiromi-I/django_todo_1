from django.db import models


class Todo(models.Model):
    title = models.CharField('タイトル', max_length=100)
    done = models.BooleanField('完 / 未完')
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title
