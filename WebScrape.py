import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

def sportsbooks_scrape(urls):
    """
    Searches different sportsbooks and returns a dictionary structured as {'Event1': ['Team1', Odds1]}

    :param
    :return: dict_web_scrape
    """
    # LOOP THROUGH PRESET URLS so we can download the game lines in HTML format
        ### soup = requests.get(url).text

            # WITHIN THE URL LOOP (SINGULAR URL AT A TIME)
            # Store all sport subcategories
            ###
            # Search for all of the instances of an event
            ###
            # Store a dictionary of {Event: 'Wager Side', odds}
            ### ??? all_h1_tags = soup.find_all(name="h1")
            ### ??? print(all_h1_tags)
            # If we only want the text within that tag, then:
            ### ??? for tag in all_h1_tags:
                ### ??? text_found = tag.getText()
                # ??? add text_found to a list
            # If we want to use the link to navigate to the
