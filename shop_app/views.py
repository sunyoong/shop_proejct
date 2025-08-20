from django.shortcuts import render, HttpResponse
from django.db.models import Prefetch
from .serializers import productSerializer
from .models import Product, Tag, ProductOption
from rest_framework import viewsets
import json

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = productSerializer

    def get_queryset(self):
        qry_set = Product.objects.all()
        if self.action in ('list', 'retrieve'):
            qry_set = (qry_set.only('pk', 'name').prefetch_related(
                Prefetch('option_set', queryset=ProductOption.objects.only("pk", "product_id", "name", "price")), 
                Prefetch('tag_set', queryset=Tag.objects.only("pk", "name"))
                ))
        return qry_set