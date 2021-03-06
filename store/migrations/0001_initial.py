# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 09:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='客户')),
                ('star', models.IntegerField(verbose_name='总体评价')),
                ('taste_score', models.IntegerField(verbose_name='口味')),
                ('environment_score', models.IntegerField(verbose_name='环境')),
                ('service_score', models.IntegerField(verbose_name='服务')),
                ('content', models.TextField(verbose_name='评价内容')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('like', models.IntegerField(verbose_name='点赞数')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='店名')),
                ('phone_number', models.CharField(max_length=50, verbose_name='电话')),
                ('address', models.TextField(verbose_name='地址')),
                ('review_number', models.IntegerField(verbose_name='评论数')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', related_query_name='review', to='store.Store'),
        ),
    ]
