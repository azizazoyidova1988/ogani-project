from django.db import connection
from contextlib import closing


def get_categories():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from category""")
        categories = dict_fetchall(cursor)
        return categories



def get_products():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product """)
        products = dict_fetchall(cursor)
        return products

def get_products_by_latest():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product  order by created_at DESC limit 3 """)
        product_price = dict_fetchall(cursor)
        return product_price


def get_products_by_price():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product  order by price DESC limit 3 OFFSET 7 """)
        product_price = dict_fetchall(cursor)
        return product_price


def get_products_by_views():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product where view > 50 order by view DESC limit 3 """)
        product_views = dict_fetchall(cursor)
        return product_views


def get_product_by_sale():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from product  where sale='-10%' limit 5 """)
        sales = dict_fetchall(cursor)
        return sales



def get_product_details(product_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*, category.name as c_name from product
        inner join category on product.category_id = category.id
        where product.id =  %s""", [product_id])
        products = dict_fetchone(cursor)
        return products

def get_product_details_by_id(category_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select product.*, category.name as c_name from product
        inner join category on product.category_id = category.id
        where category.id =  %s""", [category_id])
        products = dict_fetchall(cursor)
        return products

def get_blog():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog """)
        blog = dict_fetchall(cursor)
        return blog

def get_contact():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from contact_address """)
        contact = dict_fetchall(cursor)
        return contact

def get_blog_by_id(blog_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog where blog.id = %s """,
                       [blog_id])
        blogs = dict_fetchone(cursor)
        return blogs


def get_blog_my_post():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from blog order by created_at  limit 3  """)
        blogs = dict_fetchall(cursor)
        return blogs



def get_categories_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from max_way_category""")
        categories = dict_fetchall(cursor)
    return categories

# def get_products_count():
#     with closing(connection.cursor()) as cursor:
#         cursor.execute("""select count(name) from max_way_product""")
#         products = dict_fetchall(cursor)
#     return products
#


def get_categories_products_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(product.id),category.name,product.category_id
        FROM category LEFT JOIN product
		ON product.category_id=category.id
	GROUP BY product.category_id,category.name 
	ORDER BY COUNT(product.id) DESC""")
        categories = dict_fetchall(cursor)
        return categories


def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))
