from random import *
import random

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from product.models import Product


class DetailView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        review_count = random.randrange(2000, 3000)
        review_score = round(uniform(1, 5), 1)

        productimage = product.productimage_set.all()
        title_image_url = productimage[0].image_url
        str_title_image_url = str(title_image_url)

        allergy_list = [product_allergy.allergy.name for product_allergy in product.productallergy_set.all()]

        return JsonResponse({
            "message" : "SUCCESS",
            "name" : product.name,
            "category" : product.category.name,
            "price" : product.price,
            "desc" : product.description,
            "allergy" : allergy_list,
            "title_image_url" : str_title_image_url,
            "review_count" : review_count,
            "review_score" : review_score,
        }, status=200)
