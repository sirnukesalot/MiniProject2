# Generated by Django 4.2.16 on 2024-11-19 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('grades', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]