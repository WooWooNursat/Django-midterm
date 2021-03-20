from django.db import models
from utils.constants import JOURNAL_TYPE, JOURNAL_TYPE_BULLET

# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название')
    price = models.IntegerField(default=0, verbose_name='Цена')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    created_at = models.DateField(verbose_name='Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0, verbose_name='Количество страниц')
    genre = models.CharField(max_length=255, null=True, blank=True, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class Journal(BookJournalBase):
    type = models.SmallIntegerField(choices=JOURNAL_TYPE, default=JOURNAL_TYPE_BULLET)
    publisher = models.CharField(max_length=255, null=True, blank=True, verbose_name='Автор')

    class Meta:
        verbose_name = 'Журнал'
        verbose_name_plural = 'Журналы'
