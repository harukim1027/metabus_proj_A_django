# Generated by Django 3.2.12 on 2022-02-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('streetanimal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='protection_status',
            field=models.CharField(choices=[('1', '입양 대기'), ('2', '입양 매칭 중'), ('3', '입양 완료!')], default=1, max_length=30),
        ),
    ]