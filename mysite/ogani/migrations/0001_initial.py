# Generated by Django 3.2 on 2021-07-09 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(max_length=40, upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Contact_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('open_time', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'contact_address',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.JSONField()),
                ('total_price', models.IntegerField(default=0)),
                ('status', models.IntegerField(default=1)),
                ('payment_type', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Send_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(max_length=150)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='User_Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=100)),
                ('last_name', models.TextField(max_length=100)),
                ('country', models.TextField(max_length=30)),
                ('address', models.TextField(max_length=100)),
                ('postcode', models.CharField(max_length=30)),
                ('town_city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=40)),
                ('account_password', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user_address',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.CharField(max_length=450)),
                ('price', models.IntegerField(default=1)),
                ('old_price', models.IntegerField(default=1)),
                ('availability', models.CharField(max_length=100)),
                ('shipping', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('view', models.IntegerField(default=1)),
                ('sale', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ogani.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=850)),
                ('image', models.ImageField(upload_to='images/')),
                ('author', models.CharField(blank=True, max_length=150, null=True)),
                ('author_image', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ogani.category')),
            ],
            options={
                'db_table': 'blog',
            },
        ),
    ]
