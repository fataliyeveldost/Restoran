# Generated by Django 4.0.6 on 2022-08-02 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0002_menyu_menyu_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menyu',
            name='menyu_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
