from django.db import models
from django.contrib.auth.models import User
from films.models import Film  

class Forum(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Фильм')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ["title"]
        verbose_name = "Форум"
        verbose_name_plural = "Форумы"

    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст сообщения')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, verbose_name='Форум')

    class Meta:
        ordering = ["created_at"]
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return f"Сообщение от пользователя {self.user.username} на форуме «{self.forum.title}»"