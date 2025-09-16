from apify import Actor
from crawlee.crawlers import PlaywrightCrawler
from crawlee.http_clients import HttpxHttpClient
from .routes import router

async def main() -> None:
    """The crawler entry point."""
    async with Actor:
        crawler = PlaywrightCrawler(
            request_handler=router,
            headless=True,
            max_requests_per_crawl=10,
            http_client=HttpxHttpClient(),
        )


        await crawler.run(
            [
                'https://www.producthunt.com/',
            ]
        )
