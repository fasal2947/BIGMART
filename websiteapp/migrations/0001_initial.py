# Generated by Django 4.1.3 on 2023-01-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customrregisterdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Email', models.EmailField(blank=True, max_length=100, null=True)),
                ('Password', models.CharField(blank=True, max_length=100, null=True)),
                ('Confirmpassword', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]