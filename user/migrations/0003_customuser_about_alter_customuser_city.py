# Generated by Django 4.0 on 2021-12-30 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[['п.Караменды', 'п.Караменды'], ['г.Костанай', 'г.Костанай']], max_length=50),
        ),
    ]
