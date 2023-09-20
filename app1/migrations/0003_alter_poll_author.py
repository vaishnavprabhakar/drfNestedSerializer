# Generated by Django 4.2.5 on 2023-09-20 07:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_poll_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poll', to='app1.author'),
        ),
    ]