# Generated by Django 4.0 on 2021-12-30 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[['п.Караменды', 'п.Караменды'], ['г.Костанай', 'г.Костанай']], default=['п.Караменды', 'п.Караменды'], max_length=50),
        ),
    ]
