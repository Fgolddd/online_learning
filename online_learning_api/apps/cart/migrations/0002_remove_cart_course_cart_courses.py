# Generated by Django 5.0.4 on 2024-04-28 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('course', '0007_remove_course_attachment_path'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='course',
        ),
        migrations.AddField(
            model_name='cart',
            name='courses',
            field=models.ManyToManyField(to='course.course', verbose_name='课程'),
        ),
    ]
