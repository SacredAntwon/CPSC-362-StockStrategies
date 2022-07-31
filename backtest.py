"""

The common metrics used for backtesting include:
annualized  return  (yearly  average  %  profit  or  loss  from  the  strategy),
%  profitability  (%  of  total trades that resulted in profits),
Win/Loss ratio (sum_of_profit/sum_of_loss),
Max drawdown (the largest drop in profit and loss calculated by [trough_value – peak_value]/peak_value),
annualized volatility  (the  standard  deviation  of  daily  return  in  a  year),
Sharpe  Ratio  (the  reward/risk  ratio, calculated by an annualized return / annualized volatility)

"""

# These are the possible values that can be assigned to self.strategy in the Backtesting class
TREND_FOLLOWING_STRAT = 0
MEAN_STRAT = 1

class Backtest:

    # We have to store the list of prices for a specific ticker as a property
    # Each time the user updates the list of prices, the class must automatically update all
    #    statistical information simultaneously as described in the specification


    def __init__(self, startingBalance, priceList, strategy):

        # Save the starting balance
        self.startingBalance = startingBalance

        # Assume the ending balance is the same as the starting balance for now
        self.endingBalance = startingBalance

        # Saving the price info
        self.priceList = priceList

        # Save the number of elements in priceList as the number of days the stock was held
        # self.numDaysHeld = len(priceList)

        # Save the selected strategy (An int represending the strategy to select)
        self.strategy = strategy

        self.RunStrategy()

        # Initialize all statistical values
        """
        self.annualReturn = 0
        self.percentProfitability = 0
        self.winLossRatio = 0
        self.maxDrawdown = 0
        self.annualVolatility = 0
        self.sharpeRatio = 0
        """

    def RunStrategy(self):

        # This code runs the strategy and updates all statistics/variables upon retrieving the results

        # For now, assume that the trend following strategy is the only strategy that exists
        # This function sets up self.movAvg
        self.HundDayMovAvg()

        # This function sets up self.buySellPrices
        self.LineIntersect(self.movAvg)

        # Print these values for reference
        #print("Stock Prices: ", self.priceList)
        print("Stock Prices = [", end='')
        for i in range(len(self.priceList)):

            print(self.priceList[i], ",", end='')

        print("]")
        print()

        # Remove this later and replace with UpdateStats(); It's only temporarily for testing
        self.UpdateEndingBalance()
        self.UpdateAnnualReturn()

        print("Moving Average: ", self.movAvg)
        print("Buy/Sell Prices: ", self.buySellPrices)
        print("Starting Balance: ", self.startingBalance)
        print("Ending Balance: ", self.endingBalance)
        print("Annual Return: ", self.annualReturn)

        # Finally, call UpdateStats() to make updates to the backtesting results (TODO: Later)
        # self.UpdateStats()

    def HundDayMovAvg(self):

        # This function uses priceList to calculate the 100 day moving average and return it as a list

        # Initialize the 100 day moving average list (important, especially if the list already contains elements)
        self.movAvg = []

        # This sum is used to represent the sum of all 100 points, and can be modified to include new points
        # rather than having to sum all 100 values up again for each point
        sum = 0

        if len(self.priceList) < 100:

            # There isn't any information to return cause we haven't seen 100 days
            return []

        # Initialize sum with the first 100 prices
        for i in range(100):

            sum += self.priceList[i]

        # Save the first index since we just calulcated it
        self.movAvg.append(sum / 100)

        # From every point onward, we add a new point and remove the last point
        for i in range(100, len(self.priceList)):

            # Subtract the old price from 100 days ago
            sum -= self.priceList[i - 100]

            # Add the new price for the next day
            sum += self.priceList[i]

            # The +1 comes from the fact that we already saved the first element in movAvg
            #self.movAvg[i - 100 + 1] = sum / 100
            self.movAvg.append(sum / 100)

        # self.movAvg is now complete and ready to be used

    # linePrices - A list of all prices on a given line/set of points
    # buyStockPriceAbove - (True) buy when the stock price intersects the line and then goes ABOVE it
    #                    - (False) buy when the stock price intersects the line and then goes BELOW it
    def LineIntersect(self, linePrices, buyStockPriceAbove = True):

        # This function uses two lists of prices (self.priceList and linePrices) and finds where they intersect.
        # Depending on the value of buyStockPriceAbove, buys will be negative and sells will be positive

        # Get the number of points in the line
        # self.numDaysLine = len(linePrices)

        # Save the intersected prices as an array
        self.buySellPrices = []

        # Save whether an intersection occurred or not
        didIntersect = False

        # Save whether the stock price is above or below the strategic line or not
        stockIsAbove = False
        stockIsBelow = False

        # It shouldn't be the case that there's more days in the strategic line than in the actual stock price
        if len(linePrices) > len(self.priceList):

            print("Error! linePrices length = ", len(linePrices), "and priceList length = ", len(self.priceList))
            return []

        for i in range(len(linePrices)):

            # Check if both flags are unset
            if not stockIsBelow and not stockIsAbove:

                # Double check the flags to make sure 
                stockIsBelow = self.priceList[i + 100 - 1] < linePrices[i]
                stockIsAbove = self.priceList[i + 100 - 1] > linePrices[i]

            # Check if the stock price is above the strategic line
            if self.priceList[i + 100 - 1] > linePrices[i] and stockIsBelow:

                #print(str(self.priceList[i + 100 - 1]) + " is greater than " + str(linePrices[i]) + "!")

                # Check the buyStockPriceAbove flag to see whether we should buy or sell
                if buyStockPriceAbove:

                    # Buy the stock
                    #self.buySellPrices.append(-linePrices[i])
                    self.buySellPrices.append(-self.priceList[i + 100 - 1])

                else:

                    # Sell the stock
                    #self.buySellPrices.append(linePrices[i])
                    self.buySellPrices.append(self.priceList[i + 100 - 1])

                # Set the stockIsAbove flag to true
                stockIsAbove = True

                # Reset the stockIsBelow flag to false
                stockIsBelow = False

            # Check if the stock price is below the strategic line
            elif self.priceList[i + 100 - 1] < linePrices[i] and stockIsAbove:

                #print(str(self.priceList[i + 100 - 1]) + " is less than " + str(linePrices[i]) + "!")

                if buyStockPriceAbove:

                    # Sell the stock
                    #self.buySellPrices.append(linePrices[i])
                    self.buySellPrices.append(self.priceList[i + 100 - 1])

                else:

                    # Buy the stock
                    #self.buySellPrices.append(-linePrices[i])
                    self.buySellPrices.append(-self.priceList[i + 100 - 1])

                # Set the stockIsBelow flag to true
                stockIsBelow = True

                # Set the stockIsAbove flag to false
                stockIsAbove = False

            # Check if the stock prices are equal
            elif self.priceList[i + 100 - 1] == linePrices[i]:

                # Reset all flags
                stockIsBelow = False
                stockIsAbove = False



            """# Check if the intersection occurred
            if didIntersect:

                # Check if the stock price is above the stategic line
                if self.priceList[i + 100 - 1] > linePrices[i]:

                    # If buyStockPriceAbove is true, then we buy
                    if buyStockPriceAbove:

                        # Append the price at the line to our intersection array
                        self.buySellPrices.append(linePrices[i])

                    # This means we sell
                    else:

                        # Append the NEGATIVE price at the line to our intersection array
                        self.buySellPrices.append(-linePrices[i])

                    # Reset the status of the intersection flag
                    didIntersect = False

                # This means the stock price is below the strategic line
                elif self.priceList[i + 100 - 1] < linePrices[i]:

                    # If buyStockPriceAbove is true, then we sell
                    if buyStockPriceAbove:

                        # Append the NEGATIVE price at the line to our intersection array
                        self.buySellPrices.append(-linePrices[i])

                    # This means we sell
                    else:

                        # Append the price at the line to our intersection array
                        self.buySellPrices.append(linePrices[i])

                    # Reset the status of the intersection flag
                    didIntersect = False

            print("Comparing", round(linePrices[i], 1), "and", round(self.priceList[i + 100 - 1], 1), "...")
            if round(linePrices[i], 1) == round(self.priceList[i + 100 - 1], 1):

                # Mark the intersection for later
                didIntersect = True"""

        # self.intersectLine is now complete and ready to be used

    def UpdatePrices(self, newPriceList):

        # Update the old price list with the new price list
        self.priceList = newPriceList

    def UpdateStartingBalance(self, newStartingBalance):

        # Update the starting balance
        self.startingBalance = newStartingBalance

        # Since the starting balance changed, so do the statistics
        # self.updateStatistics()

    # We use balance and end up with self.endingBalance
    def UpdateEndingBalance(self):
        
        # Store the sum of the price of the stock at all points and eventually store the average overall price
        # priceListAvg = sum(self.priceList) / len(self.priceList)

        # Keep track of the number of shares bought/sold each time
        self.shareAmtHistory = []

        # Assume the ending balance is the same as the starting balance for now
        self.endingBalance = self.startingBalance

        # Count how many shares we own of the stock
        self.numShares = 0

        # Number of shares we can buy for our portfolio
        numSharesToGet = (0.01 * self.endingBalance) / (sum(self.priceList) / len(self.priceList))

        for sharePrice in self.buySellPrices:

            # Check if the transaction is negative (buy)
            # Check if our balance is above zero
            if sharePrice < 0 and self.endingBalance > 0:

                # Check if our balance can't afford to buy all shares
                if self.endingBalance < numSharesToGet * -sharePrice:

                    # This means the number of shares we should buy is <ending balance> / <share price>
                    self.numShares += (self.endingBalance / -sharePrice)

                    # Add the number of shares bought at this price to our share number record
                    self.shareAmtHistory.append(self.endingBalance / -sharePrice)

                    print("After this purchase I'm going to run out of money!")

                    print("Bought " + str(self.endingBalance / -sharePrice) + " shares at price: " + str(-sharePrice))

                    # Set our balance to 0, since we just spent the remaining money we had left
                    self.endingBalance = 0
                    
                    print("New Balance: " + str(self.endingBalance))

                else:

                    # Add numSharesToGet to our total number of shares
                    self.numShares += numSharesToGet

                    # Add the number of shares bought at this price to our share number record
                    self.shareAmtHistory.append(numSharesToGet)

                    print("Bought " + str(numSharesToGet) + " shares at price: " + str(-sharePrice))

                    # Subtract the transaction amount from the ending balance
                    self.endingBalance -= (numSharesToGet * -sharePrice)

                    print("New Balance: " + str(self.endingBalance))

            # The transation price is positive (can't be zero obviously) (sell)
            else:

                print("Sold " + str(self.numShares) + " shares at price: " + str(sharePrice))

                # Add the amount from selling back to our account
                self.endingBalance += (self.numShares * sharePrice)

                # Remove all shares from our account
                self.numShares = 0

                print("New Balance: " + str(self.endingBalance))

        # Check if we still own any shares, because we need to sell them and add to our balance if that's the case
        if self.numShares != 0:

            print("I'm liquidating the shares I own ( " + str(self.numShares) + " ) at price: $" + str(self.priceList[-1]) + "...")
            self.endingBalance += (self.numShares * self.priceList[-1])
            print("New Balance: " + str(self.endingBalance))

            # Remove all shares from our account
            self.numShares = 0

        # self.endingBalance is now updated


    """def updateEndingBalance(self):

        # Update the ending balance by using priceList, startingBalance and a specific strategy
        if self.strategy == TREND_FOLLOWING_STRAT:

            # Update the ending balance using the trend following strategy
            print()

        elif self.strategy == MEAN_STRAT:

            # Update the ending balance using the mean strategy
            print()

        else:

            # Print an error, since the correct strategy wasn't chosen
            print("Error! Incorrect strategy selected!")

        print()"""

    def UpdateStats(self):

        # Update the ending balance
        self.UpdateEndingBalance()

        # Update all statistics
        self.UpdateAnnualReturn()
        self.UpdatePercentProfitability()
        self.UpdateWinLossRatio()
        self.UpdateMaxDrawdown()
        self.UpdateAnnualVolatility()
        self.UpdateSharpeRatio()

    # This function is primarily for testing purposes
    def GetStats(self):

        # Print all stats
        print("Starting Balance: ", self.startingBalance)
        print("Ending Balance: ", self.endingBalance)
        print("Annual Return: ", self.annualReturn)
        print("Percent Profitability: ", "<Insert self.percentProfitability here>")
        print("Win Loss Ratio: ", "<Insert self.winLossRatio here>")
        print("Max Drawdown: ", "<Insert self.maxDrawdown here>")
        print("Annual Volatility: ", "<Insert self.annualVolatility here>")
        print("Sharpe Ratio: ", "<Insert self.sharpeRatio here>")

    def UpdateAnnualReturn(self):

        # Update the annual return variable

        # Formula: (((<Ending Balance> / <Starting Balance>) - 1)^(365 / (# of days held)) - 1) * 100

        self.annualReturn = ((self.endingBalance / self.startingBalance) ** (365 / len(self.priceList)) - 1) * 100

    def UpdatePercentProfitability(self):

        # Update the percent profitability variable

        #for i in range(len(self.buySellPrices)):



        print()

    def UpdateWinLossRatio(self):

        # Update the Win/Loss Ratio variable

        print()

    def UpdateMaxDrawdown(self):

        # Update the Win/Loss Ratio variable

        print()

    def UpdateAnnualVolatility(self):

        # Update the Annual Volatility variable

        print()

    def UpdateSharpeRatio(self):

        # Update the Sharpe Ratio variable

        print()