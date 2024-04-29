# Generated by Django 4.2.11 on 2024-04-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='is_active',
        ),
        migrations.AddField(
            model_name='item',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('REVIEW', 'Review'), ('QA', 'QA'), ('READY', 'Ready'), ('PUBLISHED', 'Published'), ('SUSPENDED', 'Suspended'), ('RETIRED', 'Retired')], default='DRAFT', max_length=10),
        ),
    ]
