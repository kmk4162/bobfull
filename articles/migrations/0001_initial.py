# Generated by Django 3.2.13 on 2022-11-30 17:37

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
            name='Matching_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('member', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grade', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='person_review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation', models.CharField(choices=[('매너가 좋았어요.', '매너가 좋았어요.'), ('제 시간에 맞춰 왔어요.', '제 시간에 맞춰 왔어요.'), ('여기는 뭐 추가?', '여기는 뭐 추가?'), ('아이디어 없음', '아이디어 없음')], max_length=80)),
                ('matching_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.matching_room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
