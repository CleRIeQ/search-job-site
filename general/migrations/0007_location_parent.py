# Generated by Django 4.0 on 2022-01-12 08:46

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0006_location_alter_jobpost_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='general.location'),
        ),
    ]
