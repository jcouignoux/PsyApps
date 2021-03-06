# Generated by Django 4.0.1 on 2022-01-05 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MR', 'Monsieur'), ('MISS', 'Mademoiselle'), ('MRS', 'Madame')], default='MR', max_length=4, verbose_name='Civilité')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nom')),
                ('first_name', models.CharField(max_length=50, verbose_name='Prénom')),
                ('phone', models.CharField(max_length=10, verbose_name='Téléphone')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Contact')),
            ],
            options={
                'verbose_name': 'Patient',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=50, verbose_name='Titre')),
                ('gender', models.CharField(choices=[('L', 'Bas'), ('M', 'Moyen'), ('H', 'Urgent')], default='L', max_length=4, verbose_name='Criticité')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Sujet',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=1000, verbose_name='Message')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.subject', verbose_name='Sujet')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Auteur')),
            ],
            options={
                'verbose_name': 'Sujet',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='Adresse')),
                ('additional_address', models.CharField(blank=True, max_length=255, verbose_name="Complément d'adresse")),
                ('postcode', models.CharField(max_length=5, verbose_name='Code postal')),
                ('city', models.CharField(max_length=50, verbose_name='Ville')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adresses',
            },
        ),
    ]
