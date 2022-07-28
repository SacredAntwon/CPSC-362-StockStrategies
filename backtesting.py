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

class Backtesting:

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
        self.numDaysHeld = len(priceList)

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
        print()

    def updatePrices(self, newPriceList):

        # Update the old price list with the new price list
        self.priceList = newPriceList

        # Upon updating the prices, the ending balance will change
        self.updateEndingBalance()

        # Update all statistics, since different prices change the starting balance
        self.updateStatistics()

    def updateStartingBalance(self, newStartingBalance):

        # Update the starting balance
        self.startingBalance = newStartingBalance

        self.updateEndingBalance()

        # Since the starting balance changed, so do the statistics
        self.updateStatistics()

    def updateEndingBalance(self):

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

        print()

    def updateStatistics(self):

        # Update all statistics
        self.updateAnnualReturn()
        self.updatePercentProfitability()
        self.updateWinLossRatio()
        self.updateMaxDrawdown()
        self.updateAnnualVolatility()
        self.updateSharpeRatio()

    def updateAnnualReturn(self):

        # Update the annual return variable

        # Formula: (((<Ending Balance> / <Starting Balance>) - 1)^(365 / (# of days held)) - 1) * 100

        self.annualReturn = (((self.endingBalance / self.startingBalance) - 1) ** (365 / self.numDaysHeld) - 1) * 100

    def updatePercentProfitability(self):

        # Update the percent profitability variable

        print()

    def updateWinLossRatio(self):

        # Update the Win/Loss Ratio variable

        print()

    def updateMaxDrawdown(self):

        # Update the Win/Loss Ratio variable

        print()

    def updateAnnualVolatility(self):

        # Update the Annual Volatility variable

        print()

    def updateSharpeRatio(self):

        # Update the Sharpe Ratio variable

        print()