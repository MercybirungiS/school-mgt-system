# Generated by Django 3.2.7 on 2021-09-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='images/')),
                ('first_name', models.CharField(max_length=12, null=True)),
                ('last_name', models.CharField(max_length=12, null=True)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Prefer not to say')], max_length=8, null=True)),
                ('age', models.PositiveSmallIntegerField(null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('nationality', models.CharField(choices=[('1', 'Rwandan'), ('2', 'Kenyan'), ('3', 'Ugandan'), ('4', 'SouthSudanes'), ('5', 'Sudanes')], max_length=15, null=True)),
                ('national_Id', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('medical_form', models.FileField(null=True, upload_to='documents/')),
                ('laptop_serial_number', models.CharField(blank=True, max_length=30, null=True)),
                ('academic_year', models.CharField(max_length=12)),
                ('course_name', models.CharField(blank=True, max_length=25, null=True)),
            ],
        ),
    ]
