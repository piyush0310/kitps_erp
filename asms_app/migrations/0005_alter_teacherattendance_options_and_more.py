# Generated by Django 5.0.4 on 2024-05-19 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asms_app', '0004_acedemiaadmin_utype_student_utype_teacher_teacher_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacherattendance',
            options={'ordering': ['date', 'teacher']},
        ),
        migrations.RemoveField(
            model_name='teacherattendance',
            name='created',
        ),
        migrations.RemoveField(
            model_name='teacherattendance',
            name='updated',
        ),
    ]
