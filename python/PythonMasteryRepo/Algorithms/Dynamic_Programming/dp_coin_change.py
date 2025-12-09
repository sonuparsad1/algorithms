"""
Title: Coin Change (Min Coins)
Topic: Dynamic Programming

Theory:
    Find minimum number of coins to make a total amount V.
    
    Recurrence:
    dp[v] = min(dp[v], dp[v - coin] + 1)
    
    Complexity: O(V * N).
"""

def coin_change(coins, amount):
    # Initialize with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
            
    return dp[amount] if dp[amount] != float('inf') else -1

def run_tests():
    coins = [1, 2, 5]
    amount = 11
    # 5 + 5 + 1 = 3 coins
    assert coin_change(coins, amount) == 3
    
    assert coin_change([2], 3) == -1
    
    print("[PASS] Coin Change")

if __name__ == "__main__":
    run_tests()
