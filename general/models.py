import datetime

from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey


class Location(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
        )

    class MPTTMeta:
        order_insertion_by = ['name']
    
    def __str__(self):
        return self.name
        

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

        
location_choices = [
    ['п.Караменды', 'п.Караменды'],
    ['г.Костанай', 'г.Костанай'],
]

premium_choices = [
    ['Нет', 'Нет'],
    ['Да', 'Да'],
]

category_choices = [
    ['Работа', 'Работа'],
    ['Подработка', 'Подработка'],
    ['Услуги', 'Услуги']
]


class JobPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    job_nature = models.CharField(max_length=300, default='', verbose_name='График')
    salary = models.PositiveIntegerField(verbose_name='Зарплата')
    premium = models.CharField(max_length=50, choices=premium_choices, default=premium_choices[1], verbose_name='Вип')
    info = models.CharField(max_length=110, verbose_name='Краткое описание', validators=[MinLengthValidator(25)])
    education = models.CharField(max_length=1000, default='', verbose_name='Образование')
    location = models.ForeignKey(
        Location,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    contact = models.CharField(max_length=200, default='', verbose_name='Контактные данные')
    requirements = models.TextField(default='', verbose_name='Требования')
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag,
                                  related_name="post",
                                    )
    published_date = models.DateTimeField(auto_now_add=True)
    paginate_by = 10


    def get_absolute_url(self):
        return reverse('single', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()
