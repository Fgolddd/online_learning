# Generated by Django 5.0.4 on 2024-04-22 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_chapter_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='course',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='course.course', verbose_name='课程'),
        ),
        migrations.RemoveField(
            model_name='chapter',
            name='video',
        ),
        migrations.AddField(
            model_name='chapter',
            name='video',
            field=models.ManyToManyField(blank=True, to='course.video', verbose_name='视频'),
        ),
    ]
