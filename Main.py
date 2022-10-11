from collections import OrderedDict
import numpy as np
import pandas as pd
from Functions import arbitrage_result
import pandas


# A dictionary to hold the teams, odds, and 
og_dict = {
    'Team1': [350, 'wager'],
    'Team2': [-120, 'wager'],
    'Team3': [1000, 'wager'],
    'Team4': [750, 'wager']
}


if __name__ == "__main__":
    
    # Declared a dictionary with wager values added
    dict_wagers = arbitrage_result(og_dict)

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
