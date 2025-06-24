import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from products.models import Product


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def sample_products(db):
    Product.objects.create(
        id=1,
        nm_id=101,
        name="Product A",
        price=1000,
        discounted_price=800,
        rating=4.5,
        reviews_count=50,
    )
    Product.objects.create(
        id=2,
        nm_id=102,
        name="Product B",
        price=2000,
        discounted_price=1800,
        rating=3.5,
        reviews_count=150,
    )
    Product.objects.create(
        id=3,
        nm_id=103,
        name="Product C",
        price=3000,
        discounted_price=2700,
        rating=5.0,
        reviews_count=10,
    )
    return Product.objects.all()


@pytest.mark.django_db
def test_get_products_no_filters(api_client, sample_products):
    url = reverse("product-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data["results"]) == 3


@pytest.mark.django_db
def test_filter_by_min_rating(api_client, sample_products):
    url = reverse("product-list")
    response = api_client.get(url, {"rating__gte": 4.0})
    assert response.status_code == 200
    results = response.data["results"]
    assert all(p["rating"] >= 4.0 for p in results)
    assert len(results) == 2  # Product A and C


@pytest.mark.django_db
def test_filter_by_price_range(api_client, sample_products):
    url = reverse("product-list")
    response = api_client.get(url, {"price__gte": 1500, "price__lte": 2500})
    assert response.status_code == 200
    results = response.data["results"]
    assert all(1500 <= float(p["price"]) <= 2500 for p in results)
    assert len(results) == 1  # Product B


@pytest.mark.django_db
def test_filter_by_reviews_count(api_client, sample_products):
    url = reverse("product-list")
    response = api_client.get(url, {"reviews_count__gte": 50})
    assert response.status_code == 200
    results = response.data["results"]
    assert all(p["reviews_count"] >= 50 for p in results)
    assert len(results) == 2  # Product A and B
