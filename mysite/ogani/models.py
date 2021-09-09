from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=40, blank=False, null=False)
    image = models.ImageField(max_length=40, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    title = models.CharField(max_length=250, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    description = models.CharField(max_length=450, blank=False, null=False)
    price = models.IntegerField(blank=False, null=False, default=1)
    old_price = models.IntegerField(blank=False, null=False, default=1)
    availability = models.CharField(blank=False, null=False,max_length=100)
    shipping = models.CharField(blank=False, null=False, max_length=50)
    weight = models.CharField(blank=False, null=False, max_length=50)
    view = models.IntegerField(default=1,blank=False, null=False)
    sale = models.CharField(max_length=10,blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "product"

    def __str__(self):
        return self.name


class User_Address(models.Model):
    first_name = models.TextField(max_length=100, blank=False, null=False)
    last_name = models.TextField(max_length=100, blank=False, null=False)
    country = models.TextField(max_length=30, blank=False, null=False)
    address = models.TextField(max_length=100, blank=False, null=False)
    postcode = models.CharField(max_length=30, blank=False, null=False)
    town_city = models.CharField(max_length=50, blank=False, null=False)
    province = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=40, blank=False, null=False)
    account_password=models.CharField(max_length=30, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_address"

    def __str__(self):
        return self.first_name

class Blog(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(max_length=850, blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    author = models.CharField(max_length=150, blank=True, null=True)
    author_image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "blog"

    def __str__(self):
        return self.title


class Contact_Address(models.Model):
    address = models.TextField(max_length=100, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    open_time = models.CharField(max_length=20, blank=False, null=False)
    email = models.EmailField(max_length=40, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "contact_address"

    def __str__(self):
        return self.address


class Send_Message(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    message = models.CharField(max_length=150, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "message"

    def __str__(self):
        return self.name


class Order(models.Model):
    products = models.JSONField(blank=False, null=False)
    total_price = models.IntegerField(blank=False, null=False, default=0)
    status = models.IntegerField(blank=False, null=False, default=1)
    payment_type = models.IntegerField(blank=False, null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order"

    def __str__(self):
        return self.products