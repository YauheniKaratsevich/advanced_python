import aiohttp
import asyncio
import os
import re
from threading import Thread
import time
import urllib.request


urls = ['https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz',
        'https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz',
        'https://www.python.org/ftp/python/3.7.2/Python-3.7.2rc1.tgz',
        'https://www.python.org/ftp/python/3.6.8/Python-3.6.8rc1.tgz',
        'https://www.python.org/ftp/python/3.7.1/Python-3.7.1.tgz',
        'https://www.python.org/ftp/python/3.6.7/Python-3.6.7.tgz',
        'https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc2.tgz',
        'https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc2.tgz',
        'https://www.python.org/ftp/python/3.7.1/Python-3.7.1rc1.tgz',
        'https://www.python.org/ftp/python/3.6.7/Python-3.6.7rc1.tgz']


def get_urls(url):
    request = urllib.request.Request(url)
    website = urllib.request.urlopen(request)
    html = str(website.read())
    links = re.findall(r'"((ht|f)tps?://\S*\.(tgz|tar\.xz))"', html)
    links = [l[0] for l in links]
    return links


def get_name(link):
    return link.split('/')[-1]


def downloader(link):
    data = urllib.request.urlopen(link)
    data_to_write = data.read()
    with open(str(get_name(link)), 'wb') as f:
        f.write(data_to_write)


def sync_dowload(links):
    for url in links:
        downloader(url)


def thread_dowload(links):
    threads = [Thread(target=downloader, args=(link,)) for link in links]

    for th in threads:
        th.start()
        th.join()


async def fetch_page(session, url):
    async with session.get(url) as response:
        content = await response.read()
        with open(str(get_name(url)), 'wb') as fd:
            fd.write(content)


async def main(links):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page(session, link) for link in links]
        await asyncio.gather(*tasks)


def rm_files(links):
    for link in links:
        try:
            os.remove(str(get_name(link)))
        except IOError:
            print("No file {}".format(str(get_name(link))))


if __name__ == '__main__':
    urls = get_urls('https://www.python.org/downloads/source/')
    print("Synchronus download: ", end="")
    st_time = time.time()
    sync_dowload(urls)
    sp_time = time.time()
    print("Done. {} files. Took {} sec.".format(len(urls), sp_time - st_time))

    rm_files(urls)

    print("Download with threads: ", end="")
    st_time = time.time()
    thread_dowload(urls)
    sp_time = time.time()
    print("Done. {} files. Took {} sec.".format(len(urls), sp_time - st_time))

    rm_files(urls)

    print("Download with aiohttp and asyncio: ", end="")
    st_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(urls))
    loop.close()
    sp_time = time.time()
    print("Done. {} files. Took {} sec.".format(len(urls), sp_time - st_time))

    rm_files(urls)
