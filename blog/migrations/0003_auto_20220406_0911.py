# Generated by Django 3.0 on 2022-04-06 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_title_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={},
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='publication_date',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tag',
            field=models.CharField(default='coding', max_length=255),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title_tag',
            field=models.CharField(max_length=255),
        ),
    ]
