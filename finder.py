#! /usr/bin/env python3

from lib import get_feed, print_section

base_url = 'http://insights.ubuntu.com'

articles = {}
articles['<none>'] = get_feed(base_url + '/feed/', none=True)
articles['Articles'] = get_feed(base_url + '/category/articles/feed/')
articles['Case studies'] = get_feed(base_url + '/category/case-studies/feed/')
articles['Events'] = get_feed(base_url + '/category/events/feed/')
articles['News'] = get_feed(base_url + '/category/news/feed/')
articles['Produce business card'] = get_feed(
    base_url + '/category/product-business-card/feed/'
)
articles['Videos'] = get_feed(base_url + '/category/videos/feed/')
articles['Webinars'] = get_feed(base_url + '/category/webinars/feed/')
articles['White papers'] = get_feed(base_url + '/category/white-papers/feed/')

print('"Section", "Categories", "URL"')

print_section(articles['<none>'])

for section in sorted(articles.keys()):
    if section != 'none':
        print_section(articles[section])
