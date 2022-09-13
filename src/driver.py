import wikipedia
from datatypes import SearchResponseEntry as Entry
from datatypes import SearchResponse as Response

Page = wikipedia.WikipediaPage


def search_pages(of: str, top: int) -> [Page]:
    """
    Search for desired page, respecting disambiguation

    :param of: The Wikipedia page to search for
    :param top: The amount of results to return in case of a disambiguation
    :return: List of Wikipedia pages
    :raises DisambiguationError: Upon trying to access a recursive disambiguation page
    :raises PageError: Upon failing to access a page in a disambiguation
    """
    try:
        out = [wikipedia.page(of)]
    except wikipedia.DisambiguationError as disambiguation:
        opt = disambiguation.options[0:top]
        out = map(wikipedia.page, opt)
    return out


def run_search(of: str, top: int) -> Response:
    """
    Search for desired page, respecting disambiguation, and construct response

    :param of: The Wikipedia page to search for
    :param top: The amount of results to return in case of a disambiguation
    :return: SearchResponse
    """
    pages   = search_pages(of, top)
    entries = list(map(page_to_entry, pages))
    return Response(results=entries)


def page_to_entry(page: Page) -> Entry:
    """
    Extract title and summary from Wikipedia page

    :param page: The relevant page
    :return: page title and summary
    """
    return Entry(title=page.title, extract=page.summary)
