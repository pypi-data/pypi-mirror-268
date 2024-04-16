import asyncio
import json
import re
from typing import Dict, Optional, List, Set, Union

# from bs4 import BeautifulSoup
# from playwright.async_api import Locator, Page
from playwright.async_api import TimeoutError as PlaywriteTimeoutError
from playwright.async_api import async_playwright, expect

from ....common.logger import logger
from ....common.storage import BaseStorage
from ....common.types import (
    CrawlerBackTask,
    CrawlerContent,
    CrawlerNop,
    DatapoolContentType,
)
from ..base_plugin import BasePlugin, WorkerTask, BaseTag

# import traceback


class WikipediaPlugin(BasePlugin):
    users: Dict[str, Optional[str]] = {}

    def __init__(self, ctx, demo_tag=False):
        super().__init__(ctx)
        self.demo_tag = BaseTag(demo_tag)

    @staticmethod
    def is_supported(url):
        u = BasePlugin.parse_url(url)
        # logger.info( f'dataphoenix.info {u=}')
        return BasePlugin.is_same_or_subdomain(u.netloc, "wikipedia.org")

    async def process(self, task: WorkerTask):
        logger.info(f"wikipedia::process({task.url})")

        async with async_playwright() as playwright:
            self.webkit = playwright.chromium
            self.browser = await self.webkit.launch()
            self.context = await self.browser.new_context()
            self.page = await self.context.new_page()
            self.history_page = await self.context.new_page()
            self.user_page = await self.context.new_page()

            logger.info(f"loading url {task.url}")
            await self.page.goto(str(task.url))

            p = BasePlugin.parse_url(task.url)
            
            if not self.demo_tag.is_valid():
                platform_tag = await self.get_platform_tag(p.netloc, self.page, 3600)
            else:
                platform_tag = self.demo_tag
            if platform_tag and platform_tag.is_crawling_allowed() is False:
                logger.info("Crawling disabled by tag")
                return

            # get text of the page as plain text
            bodys = self.page.locator("body")
            body = bodys.nth(0)
            body_text = await body.inner_text()

            # locate "History" link
            history_url_loc = await self.page.locator("#ca-history a").all()
            if len(history_url_loc) > 0:
                history_url = await history_url_loc[0].get_attribute("href")
                history_url = BasePlugin.get_local_url(history_url, task.url)
                # TODO: shared ownership to be implemented later
                #       for now use the creator of the article as the copyright owner.
                #       Commented code below is more or less valid
                # users = await self._collect_users(history_url)
                # if len(users) > 0:
                #     storage_id = BaseStorage.gen_id(task.url)
                #     logger.info(f"putting article into {storage_id=}")

                #     await self.ctx.storage.put(
                #         storage_id,
                #         json.dumps(
                #             {"body": body_text, "users": users}
                #         ),  # TODO: structure
                #     )

                # TODO: until shared ownership is not supported, we use creator of the article as the copyright owner
                creator_tag = await self._get_article_creator(history_url)
                if creator_tag and not creator_tag.is_crawling_allowed():
                    return
                if creator_tag or platform_tag:
                    storage_id = BaseStorage.gen_id(task.url)
                    logger.info(f"putting article into {storage_id=}")

                    await self.ctx.storage.put(
                        storage_id, BasePlugin.make_text_storage_value(body_text)
                    )

                    yield CrawlerContent(
                        platform_tag_id=(
                            str(platform_tag) if platform_tag is not None else None
                        ),
                        tag_id=str(creator_tag) if creator_tag is not None else None,
                        type=DatapoolContentType.Text,
                        storage_id=storage_id,
                        url=task.url,
                    )

            # parsing links as back tasks
            async for yielded in self.parse_links(self.page):
                yield yielded

    async def _get_article_creator(self, history_url) -> Optional[BaseTag]:
        """
        get the earliest user from the history list.
        """
        history_url += "&dir=prev"

        logger.info(f"loading url {history_url}")
        await self.history_page.goto(history_url)

        author_link = self.history_page.locator(".mw-userlink").last
        if await author_link.count() > 0:
            logger.info( f'got creator link {author_link=}')
            title = await author_link.get_attribute("title")
            username = title[5:]  # title structure is "User:$username"
            logger.info( f'got {username=}')
            if not username in self.users:
                href = await author_link.get_attribute("href")
                user_url = BasePlugin.get_local_url(href, history_url)
                self.users[username] = await self._parse_user_page(user_url)
            return self.users[username]

    # TODO: will be needed when shared ownership is implemented
    # async def _collect_users(self, history_url):
    #     """Collects users from article history page.
    #     Behavior depends on is_demo_mode flag.
    #     In demo mode all users are returned, in non demo mode only users with tag are returned
    #     TODO: not tested
    #     """
    #     res: Dict[str, Optional[str]] = {}  # username => tag
    #     history_url += "&limit=1000"
    #     while True:
    #         logger.info(f"loading url {history_url}")
    #         await self.history_page.goto(history_url)

    #         author_links = await self.history_page.locator(".mw-userlink").all()
    #         if len(author_links) == 0:
    #             break

    #         for link in author_links:
    #             title = await link.get_attribute("title")
    #             username = title[5:]  # title structure is "User:$username"
    #             if not username in self.users:
    #                 href = await link.get_attribute("href")
    #                 user_url = BasePlugin.get_local_url(href, history_url)
    #                 self.users[username] = await self._parse_user_page(user_url)

    #             if self.is_demo_mode or self.users[username] is not None:
    #                 res[username] = self.users[username]

    #         # link to the next batch of users
    #         next_link = await self.history_page.locator(".mw-nextlink").all()
    #         if len(next_link) == 0:
    #             break
    #         href = await next_link.get_attribute("href")
    #         history_url = BasePlugin.get_local_url(href, history_url)
    #     return res

    async def _parse_user_page(self, user_link) -> Optional[BaseTag]:
        """user_link is something like https://en.wikipedia.org/wiki/User:FrB.TG.
        Expecting tag in the text representation of the page."""
        await self.user_page.goto(user_link)
        return await BasePlugin.parse_tag_in(self.user_page, "#mw-content-text")
