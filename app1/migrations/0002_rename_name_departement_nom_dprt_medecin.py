# Generated by Django 4.2.7 on 2024-01-19 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departement',
            old_name='name',
            new_name='nom_dprt',
        ),
        migrations.CreateModel(
            name='Medecin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_med', models.CharField(max_length=50)),
                ('prenom_med', models.CharField(max_length=50)),
                ('specialite', models.CharField(max_length=50)),
                ('num_tel_med', models.FloatField(max_length=10)),
                ('Departement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.departement')),
            ],
        ),
    ]
