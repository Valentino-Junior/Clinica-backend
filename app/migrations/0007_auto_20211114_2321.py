# Generated by Django 3.2.7 on 2021-11-14 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import url_or_relative_url_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0006_growth'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergingDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desiease_name', models.CharField(max_length=200)),
                ('next_appointment', models.CharField(max_length=50)),
                ('link', url_or_relative_url_field.fields.URLOrRelativeURLField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Growth',
        ),
    ]