from django.db import models
from django.db.models import TextField, CharField, ForeignKey, IntegerField, FileField


# Create your models here.

class Categories(models.Model):
    category = CharField(max_length=20)
    parent = ForeignKey('self', on_delete=models.PROTECT, blank=True, default=None, null=True)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'


class Additions(models.Model):
    file = FileField()
    book = ForeignKey('Books', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Дополнения'
        verbose_name = 'Дополнение'


class Authors(models.Model):
    author = CharField(max_length=20)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = 'Автор'


class Tags(models.Model):
    tag = CharField(max_length=20)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'


class Books(models.Model):
    book_name = TextField(verbose_name='Книга')
    tag = models.ManyToManyField(Tags, verbose_name='Теги')
    author = models.ManyToManyField(Authors, verbose_name='Авторы')
    publication_date = CharField(max_length=12, verbose_name='Дата публикации')
    reissue_num = IntegerField(verbose_name='Номер издания')
    category = ForeignKey(Categories, on_delete=models.PROTECT, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = 'Книга'
