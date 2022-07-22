import unittest
import stockinfo

obj = stockinfo.StockInfo()

# Created a fake stock
obj.dowJones = {"FKE":
{"open": 140,
"previousClose": 145,
"bid": 20,
"ask": 15,
"volume": 69110000,
"trailingPE": 25,
"trailingEps": 5.61,
"recommend": {"firm": "Rosenblatt", "grade": "Neutral"}},
"HEY":
{"open": 142,
"previousClose": 130,
"bid": 10,
"ask": 8,
"volume": 63773878,
"trailingPE": 14,
"trailingEps": 12,
"recommend": {"firm": "Yahoo", "grade": "Buy"}}
}

class TestStock(unittest.TestCase):
    # This function tests if 1) the specified JSON file exists and 2) if JSON data could be loaded from that file
    def testGetJSONData(self):

        jsonData = obj.getJSONData('DOW.json')

        self.assertNotEqual(jsonData, None)

    # This will test if the json we made exists
    def testJSONExists(self):

        self.assertEqual(obj.fileExists('userStocks.json'), True)

    # This function tests if we get the keys from our dictionary
    def testDidGetStock(self):

        self.assertEqual(list(obj.getStockNames()), ['FKE', 'HEY'])

    # This function will check to see if clos, which is not in the dictionary
    # will return none.
    def testInvalidKey(self):

        self.assertEqual(obj.findInfo(obj.dowJones['FKE'], 'clos'), None)

    # This function will check to see if open is assigned to FKE correctly
    def testValid1Key(self):

        self.assertEqual(obj.findInfo(obj.dowJones['FKE'], 'open'), 140)

    # This function will check to see if ask is assigned to HEY correctly
    def testValid2Key(self):

        self.assertEqual(obj.findInfo(obj.dowJones['HEY'], 'ask'), 8)



if __name__ == '__main__':
    unittest.main()
