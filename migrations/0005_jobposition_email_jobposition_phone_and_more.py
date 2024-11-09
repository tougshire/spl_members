# Generated by Django 5.0.6 on 2024-11-09 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spl_members', '0004_alter_member_options_alter_member_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposition',
            name='email',
            field=models.EmailField(blank=True, help_text="The job position's email address.", max_length=254, verbose_name='email'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='phone',
            field=models.CharField(blank=True, help_text="The job positions's phone number", max_length=30, verbose_name='phone'),
        ),
        migrations.AlterField(
            model_name='member',
            name='jobposition',
            field=models.ForeignKey(blank=True, help_text="The person's job position in the organization", null=True, on_delete=django.db.models.deletion.SET_NULL, to='spl_members.jobposition', verbose_name='Job Position'),
        ),
    ]