# Generated by Django 5.1.2 on 2024-10-13 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asms_app', '0014_student_department_student_semester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='sclass',
            new_name='section',
        ),
    ]
