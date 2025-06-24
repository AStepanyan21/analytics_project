import asyncio
import logging
from asgiref.sync import sync_to_async
import httpx
from django.core.management.base import BaseCommand
from products.models import Product

logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="parse_wb_async.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

HEADERS = {"User-Agent": "Mozilla/5.0"}
BASE_URL = (
    "https://search.wb.ru/exactmatch/ru/common/v4/search"
    "?ab_testing=false&appType=1&curr=rub&dest=-1257786"
    "&query={query}&page={page}&resultset=catalog&sort=popular&spp=30"
)


class Command(BaseCommand):
    help = "Async parse Wildberries products by search query"

    def add_arguments(self, parser):
        parser.add_argument("query", type=str, help="Search keyword for Wildberries")
        parser.add_argument(
            "--pages", type=int, default=3, help="Number of pages to parse"
        )

    def handle(self, *args, **options):
        query = options["query"]
        pages = options["pages"]
        self.stdout.write(
            f"Async fetching products for query: '{query}' ({pages} pages)"
        )

        asyncio.run(self.parse_all_pages(query, pages))

    async def fetch_page(self, client: httpx.AsyncClient, query: str, page: int):
        url = BASE_URL.format(query=query, page=page)
        try:
            response = await client.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to fetch page {page}: {e}")
            return None

    @sync_to_async
    def save_products(self, products_data):
        objs = []
        created_count = 0
        for item in products_data:
            nm_id = item.get("id")
            if Product.objects.filter(nm_id=nm_id).exists():
                continue
            obj = Product(
                nm_id=nm_id,
                name=item.get("name", ""),
                price=item.get("priceU", 0) / 100,
                discounted_price=item.get("salePriceU", 0) / 100,
                rating=item.get("reviewRating", 0.0),
                reviews_count=item.get("feedbacks", 0),
            )
            objs.append(obj)
        if objs:
            Product.objects.bulk_create(objs)
            created_count = len(objs)
        return created_count

    async def parse_all_pages(self, query: str, pages: int):
        async with httpx.AsyncClient() as client:
            tasks = [
                self.fetch_page(client, query, page) for page in range(1, pages + 1)
            ]
            results = await asyncio.gather(*tasks)

        total_saved = 0
        for idx, data in enumerate(results, start=1):
            if not data:
                self.stdout.write(self.style.WARNING(f"No data on page {idx}"))
                continue
            products = data.get("data", {}).get("products", [])
            saved = await self.save_products(products)
            total_saved += saved
            self.stdout.write(self.style.SUCCESS(f"Page {idx}: saved {saved} products"))

        self.stdout.write(self.style.SUCCESS(f"Total saved products: {total_saved}"))
        logger.info(f"Async parsing done. Query: {query}, Total saved: {total_saved}")

    async def run_parse(self, query: str, pages: int):
        return await self.parse_all_pages(query, pages)
