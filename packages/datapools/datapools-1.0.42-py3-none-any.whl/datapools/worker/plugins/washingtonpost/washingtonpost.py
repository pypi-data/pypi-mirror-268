import re
import json
import requests
from bs4 import BeautifulSoup, Comment
from html2text import HTML2Text
from urllib.parse import urljoin, urlparse, urlunparse

from ....worker.utils import canonicalize_url
from ..base_plugin import BasePlugin, BaseTag, WorkerTask
from ....common.logger import logger
from ....common.storage import BaseStorage
from ....common.types import (
    CrawlerBackTask,
    CrawlerContent,
    CrawlerNop,
    DatapoolContentType,
)

DOMAIN = "www.washingtonpost.com"


class WashingtonPostPlugin(BasePlugin):

    base_url = f"https://{DOMAIN}/"

    def __init__(self, ctx, demo_tag=None):
        super().__init__(ctx)
        self.demo_tag = BaseTag( demo_tag )
        
    @staticmethod
    def is_supported( url):
        u = BasePlugin.parse_url(url)
        if u.netloc != DOMAIN:
            logger.debug(f"Validation failed - Out of domain: {url}")
            return False
        if re.match("^/subscribe/.*$", u.path):   # these pages timeout
            logger.debug(f"Validation failed - Subscription page: {url}")
            return False
        if re.match("^/people/.*$", u.path):   # there are just too many of them
            logger.debug(f"Validation failed - People page: {url}")
            return False
        return True

    def is_article(self, url):
        path = urlparse(url).path
        pattern = "^[\w\-/]{3,}/\d+/\d+/\d+/[\w-]+/$"
        return bool(re.match(pattern, path))

    def normalize(self, url):
        parts = list(urlparse(url))
        parts[5] = ""   # remove fragment
        clean_url = urlunparse(parts)
        return clean_url
          
    def extract(self, soup):
        content = soup.find("article")
        if not content:
            logger.debug(f"No <article>, trying <main>...")
            content = soup.find("main", attrs = {"data-qa": "article-body", "id": "article-body"})
        if not content:
            logger.debug(f"No <main> either. Skipped.")
            return None

        filter_list = [
            dict(string = lambda s: isinstance(s, Comment)),
            dict(name = "img"),
            dict(name = "svg"),
            dict(name = "button"),
            dict(name = "div", string = "Advertisement"),
            dict(name = "div", attrs = {"aria-roledescription": "carousel"}),
            dict(name = "div", string = "End of carousel"),
        ]
        for tag_params in filter_list:
            for element in content.find_all(**tag_params):
                element.extract()

        unwrap_tags = ["figure", "figcaption", "form", "span", "a"]
        for tag in unwrap_tags:
            for element in content.find_all(tag):
                element.unwrap()
            
        for element in content.descendants:
            if element.name:
                element.attrs = {}

        text_maker = HTML2Text(bodywidth = 80)
        text_maker.ignore_links = True
        markdown = text_maker.handle(str(content))
        markdown = re.sub("\n[ \t]+", "\n", markdown)
        markdown = re.sub("\n{2,}", "\n\n", markdown)
        
        snippet = re.sub("\n+", " ", markdown)[:160].strip()
        logger.info(f"Extracted content: {snippet}...")
        return markdown
    
    async def process(self, task: WorkerTask):
        url = task.url 
        logger.info(f"{url} - Processing... ")
        response = requests.get(url)
        if response.url != url:
            logger.info(f"{url} - Redirect to {response.url}")
            url = response.url
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        if not self.demo_tag.is_valid():
            platform_tag = await self.get_platform_tag(DOMAIN, soup, 3600)
        else:
            platform_tag = self.demo_tag

        if platform_tag and platform_tag.is_crawling_allowed() is False:
            logger.info("Crawling disabled by tag")
            return        

        logger.debug(f"Adding new links...")
        for link in soup.find_all('a', href = True):
            href = link['href']
            full_local_url = BasePlugin.get_local_url(href, url)
            if full_local_url:
                full_local_url = canonicalize_url(full_local_url)
                #logger.info(full_local_url)
                yield CrawlerBackTask(url=full_local_url)
            

        if self.is_article(url):
            content = self.extract(soup)
            if content:
                storage_id = BaseStorage.gen_id(url)
                logger.info(f"putting article into {storage_id=}")

                await self.ctx.storage.put(
                    storage_id,
                    BasePlugin.make_text_storage_value(content),
                )            
                yield CrawlerContent(
                    tag_id=str(platform_tag) if platform_tag is not None else None,
                    type=DatapoolContentType.Text,
                    storage_id=storage_id,
                    url=url,
                )

