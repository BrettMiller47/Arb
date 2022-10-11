from collections import OrderedDict
import numpy as np
import pandas as pd
from Functions import arbitrage_result
import pandas


# A dictionary to hold the teams, odds, and
starting_dict = {
    'Team1': [350, 'wager'],
    'Team2': [-120, 'wager'],
    'Team3': [1000, 'wager'],
    'Team4': [750, 'wager']
}


if __name__ == "__main__":

    # Declared a dictionary with wager values added
    dict_wagers = arbitrage_result(starting_dict)

    if len(dict_wagers) <= 1:
        print("no arbitrage opportunity")

    else:
        # Create a data frame for printing purposes
        my_df = pandas.DataFrame(dict_wagers).T

        # Rename the columns
        renamed_df = my_df.rename(columns={0: "Odds", 1: "Wagers"})

        # Round the columns
        renamed_df['Odds'] = renamed_df['Odds'].astype(int)
        renamed_df['Wagers'] = renamed_df['Wagers'].apply(
            lambda x: "${:.2f}".format(x))

        # Sum the wagers
        sum_wagers = renamed_df['Wagers'].str[1:].astype(float).sum()

        # Final Print -- data frame, Total Wagers, Min. Payout constraint used to calc. wagers
        print(renamed_df)
        print("-------------------")
        print("Total Wagers = $", sum_wagers)
        print("Min. Payout if any win = $100")
