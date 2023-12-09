import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()
        file_name = 'data.json'
        categories = []
        products = []
        category_ids={}
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        for item in data:
            if item.get('model') == 'catalog.category':
                category = {
                    'id': item.get('pk'),
                    'category_name': item.get('fields').get('category_name'),
                    'description': item.get('fields').get('description')
                }
                cat_for_create = Category(**category)
                category_ids[item.get('pk')] = cat_for_create
                categories.append(Category(**category))
        Category.objects.bulk_create(categories)
        for item in data:
            if item.get('model') == 'catalog.product':
                product = {
                    'id': item.get('pk'),
                    'prod_name': item.get('fields').get('prod_name'),
                    'description': item.get('fields').get('description'),
                    'image': item.get('fields').get('image'),
                    'category': category_ids.get(item.get('fields').get('category')),
                    'price': item.get('fields').get('price'),
                    'date_created': item.get('fields').get('date_created'),
                    'date_change': item.get('fields').get('date_change'),
                }
                products.append(Product(**product))
        Product.objects.bulk_create(products)
