# Write a function that counts how many different ways you can make change for an amount of money, given an array of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:

# 1+1+1+1, 1+1+2, 2+2.
# The order of coins does not matter:

# 1+1+2 == 2+1+1
# Also, assume that you have an infinite amount of coins.

# Your function should take an amount to change and an array of unique denominations for the coins:

#   count_change(4, [1,2]) # => 3
#   count_change(10, [5,2,3]) # => 4
#   count_change(11, [5,7]) # => 0

def count_change(money, coins):

# The number of ways you can get money with coins a, b, and c
# is the number of ways you can get (money - a), plus the number of ways
# you can get (money - b), plus the number of ways you can get (money - c).

# The number of ways you can get (money - a) with coins a, b, and c
# is the number of ways you can get ((money - a) - a), plus the number of ways
# you can get ((money - a) - b), plus the number of ways you can get ((money - a) - c).

# There is only one way to give change for 0 money with coins a, b, and c; give 0 of each.

    combos = [1] + ([0] * money)
    # combos[i] stores the number of ways you can make change for i money; combos[0] = 1,
    # values for combos[i] where i > 0 will be updated.
    for coin in coins:
        for i in range(coin, money + 1):
            # we cannot use a coin to make change for money worth less than that coin.
            combos[i] += combos[i - coin]
            # if i == coin, (i - coin) = 0; combos[0] = 1, so combos[coin] is increased by 1;
            # there is exactly 1 way to make change for the value of a coin with that coin.
            # basic insight is that number of ways you can get money with coins a, b, and c
            # is number of ways you can get (money - a) with coins a, b, and c, plus number of
            # ways you can get (money - b) with coins a, b, and c, plus number of ways you can
            # get (money - c) with coins a, b, and c.
    return combos[money]