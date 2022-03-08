from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from general.models import location_choices

from user.models import CustomUser


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Имя",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
        label="",
    )
    last_name = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Фамилия",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    username = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Имя пользователя",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    email = forms.EmailField(
        label="",
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "e-mail",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    password1 = forms.CharField(
        label="",
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Пароль",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    password2 = forms.CharField(
        label="",
        widget=forms.widgets.PasswordInput(
            attrs={
                "placeholder": "Повтор пароля",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    phone_number = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Номер телефона",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    city = forms.ChoiceField(
        label="",
        choices=location_choices,
        widget=forms.widgets.Select(
            attrs={
                "placeholder": "Город",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        ),
    )
    about = forms.CharField(
        label="",
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "О себе",
                "style": "width:300px",
                "class": "single-textarea",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'phone_number', 'city', 'about']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        label='',
        max_length=254,
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Логин",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Пароль",
                "style": "width:300px",
                "class": "single-input-primary",
            }
        )
    )


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Имя",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
        label="",
    )
    last_name = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Фамилия",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    username = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Имя пользователя",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    email = forms.EmailField(
        label="",
        widget=forms.widgets.EmailInput(
            attrs={
                "placeholder": "e-mail",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    phone_number = forms.CharField(
        label="",
        widget=forms.widgets.Input(
            attrs={
                "placeholder": "Номер телефона",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    city = forms.ChoiceField(
        label="",
        choices=location_choices,
        widget=forms.widgets.Select(
            attrs={
                "placeholder": "Город",
                "style": "width:700px",
                "class": "single-input-primary",
            }
        ),
    )
    about = forms.CharField(
        label="",
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "О себе",
                "style": "width:700px; height:210px",
                "class": "single-textarea",
            }
        ),
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'city', 'first_name', 'last_name', 'about']

