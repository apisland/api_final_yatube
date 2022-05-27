from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название группы')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор группы')
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Группы'


class Post(models.Model):
    text = models.TextField(blank=False, help_text='Текст нового поста',
                            verbose_name='Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор'
    )
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True,
        help_text='Изображение'
    )
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True,
        help_text='Группа, '
                  'к которой относится пост',
        verbose_name='Группа'
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Записи блогов'


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments',
        verbose_name='Форма комментария'
    )
    text = models.TextField(help_text='Текст нового комментария',
                            verbose_name='Текст комментария')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True,
    )


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        null=True, verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        null=True, verbose_name='Автор для подписки'
    )

    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
        constraints = [
            models.UniqueConstraint(fields=['user', 'following'],
                                    name='follow_1_time_no_self_follow')
        ]

    def __str__(self):
        return f"'Подписчик: '{self.user}', Автор : '{self.following}'"
