#maxProfit.py
"""
If you were only permitted to complete at most one transaction
(i.e., buy one and sell one share of the stock), design an algorithm
to find the maximum profit.
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6),
             profit = 6-1 = 5.
"""
#N^2 - make it better
def maxProfit(prices):
    """
        type prices: List[int]
    """
    lenp = len(prices)
    if lenp <= 1: #list is empty
        return 0

    buy = 0
    sell = 1
    mp = 0

    while buy < lenp - 1:
        if prices[buy] < prices[sell]:
            np = prices[sell] - prices[buy]
            if np > mp:
                mp = np
        sell = sell + 1
        if sell == lenp:
            buy = buy + 1
            sell = buy + 1
    return mp

print(maxProfit([1]))
print(maxProfit([1, 2, 3]))
print(maxProfit([2, 2]))
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
