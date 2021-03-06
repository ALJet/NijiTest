# Generated by Django 2.2.1 on 2019-06-18 03:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('niji', '0002_auto_20190606_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumavatar',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='uploads/forum/avatars/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]
