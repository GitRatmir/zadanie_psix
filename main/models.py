from django.db import models


class Courses(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название курса')
    content = models.TextField(blank=True, verbose_name='Контент')
    photo = models.ImageField(upload_to='photos/courses', verbose_name='Фото',blank=True)
    estimation = models.IntegerField(blank=False, verbose_name='Оценка')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Instructors(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    vor_name = models.CharField(max_length=150, verbose_name='Фамилия')
    description = models.TextField(blank=True, verbose_name='Описание')
    photo = models.ImageField(upload_to='photos/instuctors',verbose_name='Фото',blank=True)

    def __str__(self):
        return self.name + self.vor_name

    class Meta:
        verbose_name = 'Преподователь'
        verbose_name_plural = 'Преподаватели'


# Create your models here.
