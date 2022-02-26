from collections import OrderedDict


# Iterate through the WebScrape dictionary to replace American values with decimal values
def arbitrage_result(dict_american_odds):
    """ Starts with a dictionary (dict_american_odds) where Key: value pairs are {'Team': American Odds}.

        Iterates through (dict_american_odds) creating a new dictionary (dict_sorted) where Key: value pairs are
        {'Team': Wager to Win $100}.

        If the (dict_american_odds) is not an arbitrage candidate, then (dict_sorted) = {} is returned.

        P.S. - The exit of a non-profitable event must occur in the loop itself to reduce processing effort.
    :param dict_american_odds:
    :returns dict_sorted:
    """
    # Create a dictionary from the passed in dictionary.
    # Sort this new dictionary so the event's wagers are calculated in order of largest->smallest wager
    dict_sorted = dict(OrderedDict(sorted(dict_american_odds.items(), key=lambda x: x[1])))
    wagers = []

    # Change from {Team: American odds} to {Team: Revenue Rate-of-Change per $0.01 added}
    # Essentially, for each Key: Value pair in dict_sorted we are calculating the wager that payout $100
    for value in dict_sorted:

        # Iterate through each key: value pair and update with a wager as the new value
        if sum(wagers) >= 100:
            # Exit the loop if the sum of all calculated wagers is >100, the scenario is not profitable
            print("Exiting the iteration")
            dict_sorted = {}
            return dict_sorted

        else:
            # Store the absolute value of the odds in a variable to use for calculations of payout
            abs_odds_value = abs(dict_sorted[value][0])

            # Continue the loop until all key: value pairs have wagers calculated
            if dict_sorted[value][0] < 0:
                # Revenue rate of change (negative odds) = 1 / ABS(odds)
                # Wager for negative odds to payout $100 = 1 / ($0.01 + Revenue rate-of-change)
                dict_sorted[value][1] = 1 / (0.01 + (1 / abs_odds_value))
                wagers.append(dict_sorted[value][1])

            else:
                # Wager for positive odds to payout $100 = 1 / ($0.01 + (0.01 / Revenue rate-of-change / 100))
                dict_sorted[value][1] = 1 / (0.01 + (abs_odds_value / 10000))  # 10000 = $.01/100
                wagers.append(dict_sorted[value][1])

    # Return the {team: wager} dictionary
    return dict_sorted
