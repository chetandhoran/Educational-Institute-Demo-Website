# Generated by Django 5.0.1 on 2024-01-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sys_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.IntegerField()),
                ('course', models.CharField(choices=[('Web Designing', 'Web Designing'), ('Full Stack Python', 'Full Stack Python'), ('Data Science', 'Data Science'), ('Web Development', 'Web Development')], max_length=100)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
    ]
