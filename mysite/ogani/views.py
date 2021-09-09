from django.shortcuts import render, redirect
from .models import Category, Product, Contact_Address, Blog, Send_Message, User_Address
from . import servises
from django.core.paginator import Paginator, EmptyPage
from .forms import User_AddressForm,Send_MessageForm


def home(request):
    categories = servises.get_categories()
    products = servises.get_products()
    latest_products = servises.get_products_by_latest()
    pr_price = servises.get_products_by_price()
    pr_view = servises.get_products_by_views()
    blog = servises.get_blog()

    ctx = {
        'home': 'active',
        'categories': categories,
        'products': products,
        'latest_products': latest_products,
        'pr_price': pr_price,
        'pr_view': pr_view,
        'blog': blog
    }
    return render(request, 'ogani/index.html', ctx)


def blog(request):
    categories = servises.get_categories()
    blogs = servises.get_blog()
    if request.GET and request.GET.get("search"):
        blogs = Blog.objects.filter(title__icontains=request.GET.get("search"))
        print("Search", blogs)
    p = Paginator(blogs, 4)
    page_num = request.GET.get("page", 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    ctx = {
        'blog': 'active',
        'blogs': blogs,
        'categories': categories,
        'page': page,
        'page_num': page_num
    }
    return render(request, 'ogani/blog.html', ctx)


def blog_details(request, blog_id):
    blog = servises.get_blog_my_post()
    blogs = servises.get_blog()
    categories = servises.get_categories()
    blog_details = servises.get_blog_by_id(blog_id=blog_id)
    ctx = {
        'blog': blog,
        'blogs': blogs,
        'blog_details': blog_details,
        'categories': categories,
    }
    return render(request, 'ogani/blog-details.html', ctx)


def shop(request):
    categories = servises.get_categories()
    sale = servises.get_product_by_sale()
    latest_products = servises.get_products_by_latest()
    product = Product.objects.all()
    p = Paginator(product, 6)
    page_num = request.GET.get("page", 1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page = p.page(1)
    if request.GET and request.GET.get("search"):
        product = Product.objects.filter(name__icontains=request.GET.get("search"))
        print("Search", product)

    ctx = {
        'shop': 'active',
        'categories': categories,
        'latest_products': latest_products,
        'product': product,
        'sale': sale,
        "search_count": len(product),
        "search_text": request.GET.get("search"),
        'page':page,
        'page_num':page_num
    }
    return render(request, 'ogani/shop.html', ctx)


def shop_details(request, product_id):
    categories = servises.get_categories()
    products = servises.get_product_details(product_id=product_id)
    pr_view = servises.get_products_by_views()
    blogs = servises.get_blog()
    ctx = {
        'blogs': blogs,
        'categories': categories,
        'products': products,
        'pr_view': pr_view

    }
    return render(request, 'ogani/shop-details.html', ctx)


def checkout(request):
    model = User_Address()
    form = User_AddressForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print(form.errors)
    blogs = servises.get_blog()
    categories = servises.get_categories()
    ctx = {
        'blogs': blogs,
        'categories': categories

    }
    return render(request, 'ogani/checkout.html', ctx)


def shop_cart(request):
    categories = servises.get_categories()
    blogs = servises.get_blog()
    ctx = {
        'blogs': blogs,
        'categories': categories
    }
    return render(request, 'ogani/shoping-cart.html', ctx)


def contact(request):
    blogs = servises.get_blog()
    categories = servises.get_categories()
    contacts=servises.get_contact()
    model=Send_Message()
    form = Send_MessageForm(request.POST, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            print(form.errors)

    ctx = {
        'contact': 'active',
        'blogs': blogs,
        'categories':categories,
        'contacts':contacts
    }
    return render(request, 'ogani/contact.html', ctx)
