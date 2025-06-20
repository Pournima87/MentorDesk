# Generated by Django 5.2 on 2025-05-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('course_tag', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('file', models.FileField(upload_to='uploads/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
