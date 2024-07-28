# Generated by Django 4.2.5 on 2024-07-09 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_actors'),
    ]

    operations = [
        migrations.CreateModel(
            name='CensiorINFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(max_length=100, null=True)),
                ('certified_by', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='censior_details',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie', to='movies.censiorinfo'),
        ),
    ]
