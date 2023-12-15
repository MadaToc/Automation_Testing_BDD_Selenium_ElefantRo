"""
These tests cover AskserchPage searches.
"""

from pages.result import AskResultPage
from pages.search import AskSearchPage


def test_basic_askpage_search(browser):
    search_page = AskSearchPage(browser)
    result_page = AskResultPage(browser)
    PHRASE = "panda"

    # Given the Ask.com home page is displayed
    search_page.load()

    # When the user searches for "panda"
    search_page.search(PHRASE)

    # Then the search result title contains "panda"
    assert PHRASE in result_page.title()

    # And the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()
