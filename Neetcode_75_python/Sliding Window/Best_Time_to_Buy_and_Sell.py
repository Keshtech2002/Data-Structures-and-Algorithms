def maxProfit(prices: list[int]) -> int:
    """
    Problem:
      You are given an array prices where prices[i] is the price of a stock on the i-th day.
      You want to maximize your profit by choosing a single day to buy one stock and a different day in the future to sell it.
      Return the maximum profit you can achieve. If no profit is possible, return 0.

    Approach:
      - Use two pointers:
        * l (left) = index of the day we might buy.
        * r (right) = index of the day we might sell.
      - Iterate through prices with r:
        * If prices[r] > prices[l]: calculate profit (sell on r, buy on l),
          update maxP if profit is higher.
        * Otherwise (prices[r] <= prices[l]): shift l to r (new potential buying day).
      - Keep track of the maximum profit throughout.

    Time Complexity: O(n) — single pass through prices.
    Space Complexity: O(1) — only variables l, r, and maxP used.

    Example:
      prices = [7,1,5,3,6,4]
      - Buy at 1 (index 1), sell at 6 (index 4) → profit 5.
      → Returns 5.
    """

    # Initialize two pointers: 
    # l = potential buying day index
    # r = potential selling day index
    l, r = 0, 1  # left=buy, right=sell
    maxP = 0     # track the maximum profit found so far

    # Iterate while the right pointer is within bounds
    while r < len(prices):
        # Case 1: current price at r is greater than at l → possible profit
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]  # profit from buying at l, selling at r
            maxP = max(maxP, profit)        # update max profit if this profit is larger
        else:
            # Case 2: price at r is less or equal → new potential buying day
            l = r                          # shift l to r (cheaper stock to buy)

        # Move r to the next day regardless
        r += 1

    return maxP  # return the maximum profit found

if __name__ == "__main__":
    print(maxProfit([10,1,5,6,7,1]))