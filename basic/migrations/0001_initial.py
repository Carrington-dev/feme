# Generated by Django 4.1.4 on 2023-01-24 12:39

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
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=400)),
                ('message', models.TextField()),
                ('date_recieved', models.DateTimeField(auto_now_add=True, verbose_name='date recieved')),
                ('date_last_viewed', models.DateTimeField(auto_now=True, verbose_name='last viewed')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='email')),
                ('is_subscribed', models.BooleanField(default=True, verbose_name='subscribed')),
                ('date_recieved', models.DateTimeField(auto_now_add=True, verbose_name='date recieved')),
                ('date_last_viewed', models.DateTimeField(auto_now=True, verbose_name='last viewed')),
            ],
            options={
                'verbose_name': 'Subscribe',
                'verbose_name_plural': 'Subscribes',
            },
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(help_text='9708098714087', max_length=200)),
                ('full_name', models.CharField(max_length=300, verbose_name='Enter your full name')),
                ('email', models.EmailField(max_length=30)),
                ('contact', models.CharField(help_text='012 270 2333', max_length=20)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('membership', models.CharField(choices=[('Job/Learnship Seeker', 'Job/Learnship Seeker'), ('Business data', 'Business data'), ('CIPC Registered Company', 'CIPC Registered Company')], default='Job/Learnship Seeker', max_length=200)),
                ('best_calltime', models.CharField(choices=[('Morning', 'Morning'), ('Evening', 'Evening'), ('Afternoon', 'Afternoon'), ('Weekends', 'Weekends')], default='Morning', max_length=200)),
                ('company_name', models.CharField(blank=True, max_length=300, null=True, verbose_name='Enter your company name')),
                ('registration_number', models.CharField(blank=True, max_length=60, null=True)),
                ('age', models.IntegerField(help_text='Your age')),
                ('company_address', models.CharField(blank=True, max_length=200, null=True)),
                ('business_size', models.CharField(choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Micro', 'Micro')], default='Small', max_length=200)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('industry', models.CharField(blank=True, max_length=200, null=True)),
                ('have_record', models.BooleanField(default=False, help_text='Do you have a criminal record?')),
                ('can_recieve_updates', models.BooleanField(default=True, help_text='Do you grant FAN permission to utIlize your company information for marketing purposes?')),
                ('allow_data_access', models.BooleanField(default=True, help_text='Do you allow FAN access to your CIPC business portal for purposes of accessing supporting documents?')),
                ('date_applied', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Network',
                'verbose_name_plural': 'Networks',
            },
        ),
    ]