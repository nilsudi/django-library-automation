# Generated by Django 4.2.6 on 2023-12-11 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_books_books_users_books'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorId', models.IntegerField(unique=True)),
                ('author_name', models.CharField(max_length=250)),
                ('birth_year', models.IntegerField()),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='users.books')),
            ],
        ),
    ]
