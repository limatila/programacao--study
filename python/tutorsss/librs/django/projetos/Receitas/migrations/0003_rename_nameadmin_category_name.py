# Generated by Django 5.1.1 on 2024-10-31 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas', '0002_category_nameadmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='nameAdmin',
            new_name='name',
        ),
    ]
