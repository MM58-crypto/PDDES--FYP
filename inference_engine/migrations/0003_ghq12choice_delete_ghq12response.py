# Generated by Django 4.1.5 on 2023-03-30 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inference_engine', '0002_rename_ghq12_response_ghq12response'),
    ]

    operations = [
        migrations.CreateModel(
            name='GHQ12Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inference_engine.ghq12question')),
            ],
        ),
        migrations.DeleteModel(
            name='GHQ12Response',
        ),
    ]
