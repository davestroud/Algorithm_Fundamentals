def solution(n):
    # your code here
    memo = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    return staircase(1, n, memo) - 1

def staircase(h, l, memo):
    if memo[h][l] != 0:
        return memo[h][l]
    if l == 0:
        return 1
    if l < h:
        return 0
    memo[h][l] = staircase(h + 1, l - h, memo) + staircase(h + 1, l, memo)
    return memo[h][l]