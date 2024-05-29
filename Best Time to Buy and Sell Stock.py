def maxProfit(prices: list[int]) -> int:
    profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] > prices[i] and prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
    return profit

# more efficient way with O(n) complexity
def maxProfit(prices: list[int]) -> int:
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] < buy:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit
