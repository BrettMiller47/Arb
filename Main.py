from collections import OrderedDict
import numpy as np
import pandas as pd
from Functions import arbitrage_result
import pandas
from WebScrape import sportsbooks_scrape


# dict_web_scrape is the output of WebScrape.py
# TEMPORARILY THIS IS THE SETUP (WAIT FOR WEB SCRAPE TO TRULY SET UP FUNCTIONS.PY)
# WE WANT THE SCRIPT TO WORK TO PRINT A DF SUMMARY, THEN REMOVE "Event" and replace with "Team"
# We can limit dict_web_scrape to identify only 1 event, because wagers will be placed manually (can rerun after)
# Assume arbitrage opportunities are rare and there's no need to weigh the opportunity cost of one vs another
predifined_urls = {
    'Draftkings': 'https://sportsbook.draftkings.com/featured?category=game-lines',
    'Fanduel': 0,
    'Fox': 0,
    'BetMGM': 1,
    'Ceasars': 1,
    'Barstool': 0,
    'TwinSpires': 0,
    'Parx': 0,
    'UniBet': 0,
    'BetRivers': 0
}

dict_web_scrape = {
    'Team1': [350, 'wager'],
    'Team2': [-120, 'wager'],
    'Team3': [1000, 'wager'],
    'Team4': [750, 'wager']
}

print(dict_web_scrape)


# dict_web_scrape feeds the arbitrage_result() function and returns either
# - blank dictionary (no arbitrage opportunity)
# or
# - dictionary structured asa {'Team1': [Odds, 'Wager']}
if __name__ == "__main__":
    dict_wagers = arbitrage_result(dict_web_scrape)

    if len(dict_wagers) <= 1:
        print("no arbitrage opportunity")

    else:
        # Create a dataframe for a summary print of the wagering event
        my_df = pandas.DataFrame(dict_wagers).T
        print(my_df)

        # Rename the columns appropriately
        renamed_df = my_df.rename(columns={0: "Odds", 1: "Wagers"})

        # Round the columns appropriately
        renamed_df['Odds'] = renamed_df['Odds'].astype(int)
        renamed_df['Wagers'] = renamed_df['Wagers'].apply(lambda x: "${:.2f}".format(x))

        # Create variables for formatting final print
        total_wagers_print = renamed_df['Wagers'].str[1:].astype(float).sum()

        # Final Print
        print(renamed_df)
        print("Total Wagers = $", total_wagers_print)
        print("Min. Payout if any win = $100")
