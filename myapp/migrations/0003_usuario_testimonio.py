# Generated by Django 3.1.2 on 2020-12-04 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_usuario_testimonio'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='testimonio',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
