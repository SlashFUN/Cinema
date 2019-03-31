# Generated by Django 2.1.7 on 2019-03-30 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the film's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this film', to='catalog.Genre'),
        ),
        migrations.AlterField(
            model_name='filmrent',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Film availability', max_length=1),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Language'),
        ),
    ]
