# Generated by Django 4.1 on 2022-09-06 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('subtitle', models.CharField(max_length=250)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('header1', models.CharField(max_length=100)),
                ('image1', models.FileField(upload_to='images/gallery')),
                ('text1', models.TextField()),
                ('header2', models.CharField(max_length=100)),
                ('image2', models.FileField(upload_to='images/gallery')),
                ('text2', models.TextField()),
                ('header3', models.CharField(max_length=100)),
                ('image3', models.FileField(upload_to='images/gallery')),
                ('text3', models.TextField()),
                ('header4', models.CharField(max_length=100)),
                ('image4', models.FileField(upload_to='images/gallery')),
                ('text4', models.TextField()),
                ('header5', models.CharField(max_length=100)),
                ('image5', models.FileField(upload_to='images/gallery')),
                ('text5', models.TextField()),
                ('header6', models.CharField(max_length=100)),
                ('text6', models.TextField()),
                ('header7', models.CharField(max_length=100)),
                ('text7', models.TextField()),
                ('header8', models.CharField(max_length=100)),
                ('text8', models.TextField()),
                ('header9', models.CharField(max_length=100)),
                ('text9', models.TextField()),
                ('header10', models.CharField(max_length=100)),
                ('text10', models.TextField()),
                ('categories', models.ManyToManyField(related_name='posts', to='blog.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=60)),
                ('body', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]
