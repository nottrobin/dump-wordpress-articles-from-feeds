from feedparser import parse


def get_feed(url, none=False):
    articles = []
    page = 1
    empty_page = False

    while not empty_page:
        feed_url = url + '?paged=' + str(page)
        insights_feed = parse(feed_url)

        page = page + 1

        if len(insights_feed['entries']) == 0:
            empty_page = True
        else:
            for entry in insights_feed['entries']:
                if 'tags' in entry:
                    if none:
                        continue
                    else:
                        section = entry['tags'].pop(0)['term']
                        categories = entry['tags']
                else:
                    if none:
                        section = "<none>"
                        categories = []
                    else:
                        raise Exception('No category')

                data = {
                    "section": section,
                    "url": entry['link']
                }
                if len(categories) > 0:
                    data['categories'] = ", ".join(
                        [tag['term'] for tag in categories]
                    )
                else:
                    data['categories'] = "<none>"

                articles.append(data)

    return articles


def print_item_row(item):
    print (
        '"{section}", "{categories}", "{url}"'.format(
            section=item['section'],
            categories=item['categories'],
            url=item['url']
        )
    )


def print_section(items):
    sorted_section = sorted(
        items,
        key=lambda item: item['categories']
    )

    for item in sorted_section:
        if item['categories'] == '<none>':
            print_item_row(item)

    for item in sorted_section:
        if item['categories'] == '<none>':
            continue
        print_item_row(item)
