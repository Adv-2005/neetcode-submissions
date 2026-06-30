class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit=0
        minPrice= 10000
        for price in prices:
            if price<minPrice:
                minPrice=price
            if price-minPrice>maxProfit:
                maxProfit= price-minPrice
        return maxProfit