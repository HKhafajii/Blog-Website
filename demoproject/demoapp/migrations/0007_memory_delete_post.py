# Generated by Django 5.0.4 on 2024-05-06 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_alter_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='users', to='demoapp.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]