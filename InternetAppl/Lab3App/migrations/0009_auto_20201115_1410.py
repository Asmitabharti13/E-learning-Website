# Generated by Django 3.1.2 on 2020-11-15 19:10

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Lab3App', '0008_activity_club'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewer', models.EmailField(max_length=254)),
                ('rating', models.PositiveIntegerField()),
                ('comments', models.TextField(blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab3App.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
    ]
