# Generated by Django 3.2.13 on 2022-12-13 15:29

import articles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matching_room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('to_date', models.DateTimeField()),
                ('content', models.TextField()),
                ('member', models.ManyToManyField(related_name='members', to=settings.AUTH_USER_MODEL)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('grade', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reviewimages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to=articles.models.image_upload_path)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewimage', to='articles.review')),
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
