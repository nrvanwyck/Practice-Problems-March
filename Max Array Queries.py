def maxArrayQueries(n, queries):
    zeroes = [0 for i in range(n + 1)]
    for query in queries:
        zeroes[query[0] - 1] += query[2]
        zeroes[query[1]] -= query[2]
    current = 0
    maximum = current
    for i in range(len(zeroes)):
        current += zeroes[i]
        if current > maximum:
            maximum = current
    print(zeroes)
    return maximum
