from collections import OrderedDict


# Iterate through the WebScrape dictionary to replace American values with decimal values
def arbitrage_result(dict_american_odds):
    """ Starts with a dictionary of American sports betting odds where Key: value pairs are {'Team': American Odds}.

        Iterates through (dict_american_odds) creating a new dictionary (dict_sorted) where Key: value pairs are
        {'Team': Wager to Win $100}.

        If the (dict_american_odds) is not an arbitrage candidate, then (dict_sorted) = {} is returned.

    :param dict_american_odds: {'Team': American Odds}
    :returns dict_sorted:  {'Team': Wager to Win $100}
    """
    # Create and sort the argument dictionary such that the event's wagers will be largest --> smallest
    dict_sorted = dict(OrderedDict(sorted(dict_american_odds.items(), key=lambda x: x[1])))
    wagers = []

    # For each dict_sorted odds, calculate the wager required for a $100 winning payout (including original stake)
    for value in dict_sorted:

        # Iterate through each key: value pair and update with a wager as the new value
        if sum(wagers) >= 100:
            # Exit the loop if the sum of all calculated wagers is >100, the scenario is not profitable
            print("Darn!  No arbitrage opportunity.")
            dict_sorted = {}
            return dict_sorted

        else:
            # Get the absolute value of the odds
            abs_odds_value = abs(dict_sorted[value][0])

            # Continue the loop until all odds offers have a calculated wager for $100 payout (including original stake)
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
