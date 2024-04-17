"""
These tests cover DuckDuckGo searches.
"""
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):
  search_page = DuckDuckGoSearchPage(browser)
  result_page = DuckDuckGoResultPage(browser)
  PHRASE = "panda"
  # Given the DuckDuckGo home page is displayed
  # TODO
  search_page.load()

  # When the user searches for "panda"
  # TODO
  search_page.search(PHRASE)

  # Then the search result title contains "panda"
  # TODO
  assert PHRASE in result_page.title()

  # And the search result query is "panda"
  # TODO
  assert PHRASE == result_page.search_input_value()

  # And the search result links pertain to "panda"
  # TODO
  for title in result_page.result_link_titles():
    assert PHRASE.lower() in title.lower()

  raise Exception("Incomplete Test")
