# Generated by Django 4.0 on 2022-02-04 07:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0010_alter_jobpost_published_date_alter_jobpost_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 2, 4, 13, 0, 46, 688799)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='tags',
            field=models.ManyToManyField(related_name='post', to='general.Tag'),
        ),
    ]
