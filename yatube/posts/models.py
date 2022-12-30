from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='title')
    slug = models.SlugField(unique=True, verbose_name='slug')
    description = models.TextField(verbose_name='description')

    def str(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='text')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='pub_date')
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE,
        verbose_name='author'
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        related_name='posts',
        on_delete=models.SET_NULL,
        verbose_name='group'
    )

    def str(self):
        return self.text
