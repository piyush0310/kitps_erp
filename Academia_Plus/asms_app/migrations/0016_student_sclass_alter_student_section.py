# Generated by Django 5.1.2 on 2024-10-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asms_app', '0015_rename_sclass_student_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='sclass',
            field=models.CharField(default='default_value', max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='section',
            field=models.CharField(default='General', max_length=50),
        ),
    ]
