#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
def max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# Test cases
test_cases = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1],
    [1, 2, 3, 4, 5]
]

for i, prices in enumerate(test_cases, 1):
    print(f"Test Case {i}: {max_profit(prices)}")
