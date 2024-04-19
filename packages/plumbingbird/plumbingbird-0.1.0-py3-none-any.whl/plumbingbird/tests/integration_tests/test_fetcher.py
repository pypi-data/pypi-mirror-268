import pytest
from ..demo.dummy_api_fetcher import DummyJSON
from collections.abc import Generator


@pytest.fixture
def api_fetcher():
    return DummyJSON(endpoint="products", parse_key="products")


def test_conn(api_fetcher):
    sesh = api_fetcher.connect()
    assert sesh
    assert sesh.auth
    response = sesh.get(api_fetcher.base_url)
    assert response.ok


def test_fetch(api_fetcher):

    result_iter = api_fetcher.fetch()
    assert isinstance(result_iter, Generator)
    should_be = {
        "id": 1,
        "title": "iPhone 9",
        "description": "An apple mobile which is nothing like apple",
        "price": 549,
        "discountPercentage": 12.96,
        "rating": 4.69,
        "stock": 94,
        "brand": "Apple",
        "category": "smartphones",
        "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
        "images": [
            "https://cdn.dummyjson.com/product-images/1/1.jpg",
            "https://cdn.dummyjson.com/product-images/1/2.jpg",
            "https://cdn.dummyjson.com/product-images/1/3.jpg",
            "https://cdn.dummyjson.com/product-images/1/4.jpg",
            "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
        ],
    }
    assert next(result_iter) == should_be


def test_fetch_all(api_fetcher):

    result_iter = api_fetcher.fetch()
    all_results = [line for line in result_iter]

    assert len(all_results) == 100
