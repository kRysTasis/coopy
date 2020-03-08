# Generated by Django 3.0.3 on 2020-03-08 10:07

import blog.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', blog.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccessAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_pk', models.PositiveIntegerField(blank=True, null=True, verbose_name='Blog Pk')),
                ('blog_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Blog Name')),
                ('blog_owner', models.CharField(blank=True, max_length=30, null=True, verbose_name='Blog Owner')),
                ('blog_url', models.URLField(blank=True, null=True, verbose_name='Blog Url')),
                ('total_pv', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total PV')),
                ('month_pv', models.PositiveIntegerField(blank=True, null=True, verbose_name='Monthly PV')),
                ('week_pv', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weekly PV')),
                ('day_pv', models.PositiveIntegerField(blank=True, null=True, verbose_name='Daily PV')),
                ('total_user', models.PositiveIntegerField(blank=True, null=True, verbose_name='Total User')),
                ('month_user', models.PositiveIntegerField(blank=True, null=True, verbose_name='Monthly User')),
                ('week_user', models.PositiveIntegerField(blank=True, null=True, verbose_name='Weekly User')),
                ('day_user', models.PositiveIntegerField(blank=True, null=True, verbose_name='Daily User')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_pk', models.PositiveIntegerField(verbose_name='Blog Pk')),
                ('blog_name', models.CharField(max_length=50, verbose_name='Blog Title')),
                ('blog_owner', models.CharField(max_length=30, verbose_name='Blog Owner')),
                ('blog_url', models.URLField(verbose_name='Blog Url')),
                ('uuId', models.UUIDField(editable=False, verbose_name='Uuid')),
                ('ip', models.GenericIPAddressField(unpack_ipv4=True, verbose_name='IP Address')),
                ('page', models.URLField(max_length=300, verbose_name='Page')),
                ('user', models.CharField(max_length=30, verbose_name='User')),
                ('timezone', models.CharField(max_length=30, verbose_name='Timezone')),
                ('language', models.CharField(max_length=30, verbose_name='Language')),
                ('device', models.CharField(max_length=50, verbose_name='Device')),
                ('now', models.CharField(max_length=30, verbose_name='Now')),
                ('referer', models.CharField(blank=True, max_length=300, null=True, verbose_name='Referer')),
                ('browser', models.CharField(max_length=50, verbose_name='Browser')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='未分類', max_length=50, verbose_name='Category')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('slug', models.SlugField(default=models.CharField(default='未分類', max_length=50, verbose_name='Category'))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Blog Title')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('url', models.SlugField(verbose_name='Url')),
                ('icon', models.ImageField(upload_to='upload/test', verbose_name='Icon')),
                ('temp_no', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Tag')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('slug', models.SlugField(default=models.CharField(max_length=50, verbose_name='Tag'))),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Content')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='upload/test/', verbose_name='Thumbnail')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('isPublic', models.BooleanField(default=False, verbose_name='Publish or Not')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category')),
                ('related_articles', models.ManyToManyField(blank=True, related_name='_post_related_articles_+', to='blog.Post')),
                ('tags', models.ManyToManyField(blank=True, to='blog.Tag')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(verbose_name='Text')),
                ('email', models.EmailField(blank=True, max_length=255, verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('is_public', models.BooleanField(default=False, verbose_name='Publish or Not')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]