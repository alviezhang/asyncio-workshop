# 3_3.py
# Another concurrent crawler with limit


import asyncio

import aiohttp
import lxml.html
from urllib.parse import urljoin


CONCURRENT = 2


async def fetch(url):
    print(f"fetching url: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                raise ValueError(f"http code: {response.status}")
            body = await response.read()
            print(f"fetched url: {url}")
            return body


def parse_body(content: str):
    doc_tree = lxml.html.fromstring(content)
    search_result = doc_tree.xpath('//*[@id="mw-content-text"]')

    if not search_result:
        return None

    content_tree = search_result[0]
    return content_tree


def get_links(html_tree):
    links = []
    for a_tag in html_tree.xpath('//a[starts-with(@href, "/wiki/")]'):
        links.append(urljoin("https://en.wikipedia.org", a_tag.attrib["href"]))
    return links


async def crawl(links):
    # TODO
    # Lock-free code here
    ...


async def main():
    content = await fetch("https://en.wikipedia.org/wiki/Python")

    # here is link list to be crawled
    links = get_links(parse_body(content))

    await crawl(links)


if __name__ == "__main__":
    asyncio.run(main())
