# Generated by Django 5.1 on 2024-08-25 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademyApp', '0002_alter_student_slot1date_alter_student_slot2date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='paid',
            field=models.IntegerField(default=0),
        ),
    ]
