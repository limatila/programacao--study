# Generated by Django 5.1.1 on 2024-11-07 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Receitas', '0008_alter_receita_imagereceita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='idCategory',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='receita',
            name='idPage',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
