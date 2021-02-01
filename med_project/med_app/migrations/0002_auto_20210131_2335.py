# Generated by Django 3.1.5 on 2021-01-31 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('hp', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Pokemmon',
        ),
    ]
