# Generated by Django 4.2.7 on 2024-02-05 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('face_recognition_app', '0003_student_excel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='excel_file',
        ),
    ]
