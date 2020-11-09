# Generated by Django 3.1.2 on 2020-11-09 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendManagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='number_people_scoring',
        ),
        migrations.RemoveField(
            model_name='product',
            name='overall_score',
        ),
        migrations.AddField(
            model_name='product',
            name='number_people_scoring_five',
            field=models.IntegerField(default=0, verbose_name='number_people_scoring_five'),
        ),
        migrations.AddField(
            model_name='product',
            name='number_people_scoring_four',
            field=models.IntegerField(default=0, verbose_name='number_people_scoring_four'),
        ),
        migrations.AddField(
            model_name='product',
            name='number_people_scoring_one',
            field=models.IntegerField(default=0, verbose_name='number_people_scoring_one'),
        ),
        migrations.AddField(
            model_name='product',
            name='number_people_scoring_three',
            field=models.IntegerField(default=0, verbose_name='number_people_scoring_three'),
        ),
        migrations.AddField(
            model_name='product',
            name='number_people_scoring_two',
            field=models.IntegerField(default=0, verbose_name='number_people_scoring_two'),
        ),
    ]
