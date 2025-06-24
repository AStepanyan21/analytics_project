from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.schemas import AutoSchema
from drf_spectacular.utils import extend_schema

from django.shortcuts import render


def index(request):
    return render(request, "products/index.html")


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        "price": ["gte", "lte"],
        "rating": ["gte"],
        "reviews_count": ["gte"],
    }
    ordering_fields = ["price", "rating", "reviews_count", "name"]

    @extend_schema(summary="Get filtered list of products")
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
