from django import forms
from django.core.validators import MinLengthValidator
from django.forms.widgets import TextInput
from django.contrib.auth.models import User

from general.models import JobPost, Category, Location, Tag

tags = Tag.objects.all()


class NewPostForm(forms.ModelForm):
    title = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Заголовок",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    requirements = forms.CharField(
        label="",
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Основная часть",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    info = forms.CharField(
        label="",
        max_length=200,
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Короткое описание (25-110 символов)",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    education = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Образование",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    job_nature = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Расписание-ставка",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    contact = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Контактные данные",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    salary = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Оплата",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    location = forms.ModelChoiceField(
        label="",
        queryset=Location.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Город",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )

    category = forms.ModelChoiceField(
        label="",
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={
                "placeholder": "Категория",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )

    tags = forms.ModelMultipleChoiceField(
        label="",
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(
            attrs={
                "placeholder": 'Теги',
                "style": "width:700px",
                "class": "single-input-primary",
            }
        )
    )

    class Meta:
        model = JobPost
        fields = ('title', 'requirements', 'info',  'education', 'job_nature', 'contact', 'salary',  'location', 'category', 'tags')




