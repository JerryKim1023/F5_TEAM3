# Generated by Django 4.0.3 on 2022-03-22 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Datcle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=200)),
                ('like_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('like_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CommentLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(db_column='comment', on_delete=django.db.models.deletion.CASCADE, to='likeapp.datcle')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='likeapp.author')),
            ],
            options={
                'db_table': 'comment_likes',
            },
        ),
        migrations.CreateModel(
            name='ArticleLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article', models.ForeignKey(db_column='article', on_delete=django.db.models.deletion.CASCADE, to='likeapp.post')),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, to='likeapp.author')),
            ],
            options={
                'db_table': 'article_likes',
            },
        ),
        migrations.AddConstraint(
            model_name='commentlikes',
            constraint=models.UniqueConstraint(fields=('user', 'comment'), name='unique_user_comment'),
        ),
        migrations.AddConstraint(
            model_name='articlelikes',
            constraint=models.UniqueConstraint(fields=('user', 'article'), name='unique_user_article'),
        ),
    ]
