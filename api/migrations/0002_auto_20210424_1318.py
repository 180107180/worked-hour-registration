# Generated by Django 3.2 on 2021-04-24 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='absenserecord',
            name='employee',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='absent_records', to='api.employee'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='auth_emp1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emp1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='employee',
            name='auth_emp2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='emp2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='record',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='records', to='api.employee'),
            preserve_default=False,
        ),
    ]
