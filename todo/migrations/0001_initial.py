# Generated by Django 3.1.3 on 2021-02-02 08:24

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, max_length=31, populate_from=['name'])),
                ('task_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['task_date'],
            },
        ),
    ]
