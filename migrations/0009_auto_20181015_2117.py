# Generated by Django 2.1 on 2018-10-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0008_quote_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campus',
            name='campus_fax',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='campus',
            name='campus_phone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
