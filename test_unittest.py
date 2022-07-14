import unittest
import stockinfo

class TestStock(unittest.TestCase):

    def testGetJSONData(self):

        # This function tests if 1) the specified JSON file exists and 2) if JSON data could be loaded from that file

        jsonData = stockinfo.getJSONData('DOW.json')

        self.assertNotEqual(jsonData, None)

    def testDidGetStock(self):

        # This function tests to make sure that getStockNames can retrieve at least one stock

        jsonData = stockinfo.getJSONData('DOW.json')

        numStocks = 1

        self.assertNotEqual(stockinfo.getStockNames(numStocks, jsonData), dict())

    def testDidGetNStocks(self):

        jsonData = stockinfo.getJSONData('DOW.json')

        numStocks = 8

        self.assertEqual(len(stockinfo.getStockNames(numStocks, jsonData).keys()), numStocks)

    def testInvalidStockNumber(self):

        jsonData = stockinfo.getJSONData('DOW.json')

        numStocks = 0

        self.assertEqual(stockinfo.getStockNames(numStocks, jsonData), dict())

        numStocks = -1

        self.assertEqual(stockinfo.getStockNames(numStocks, jsonData), dict())

        numStocks = 31

        self.assertEqual(stockinfo.getStockNames(numStocks, jsonData), dict())

if __name__ == '__main__':
    unittest.main()