# There are N people, numbered from 0 to N-1, playing a game. The K-th person is assigned the letter S[K].
# * At the beginning the oth person sends a message, consisting of a single letter S[0], to the A[O]-th person.
# * When the K-th person receives the message, they append their letter S[K] to the message and forward it to A[K].
# * The game ends when the oth person receives the message. Find the final message.
# * You can assume that A contains every integer from 0 to N-1 exactly once.
# * Write a function: def solution(S, A) that given a string S and an array of
# * integers A, both of length N, returns a string denoting the final message received by the Oth person.
# *
# * Examples:
# * 1. Given S = "cdeo" and A = [3, 2, 0, 1), your function should returns "code".


S = "cdeo"
A = [3,2,0,1]

S = "cdeenetpi"
A = [5,2,0,1,6,4,8,3,7]

res = S[0]
flag = True
ind =A[0]

while flag:
    
    res += (S[ind])

    ind = A[ind]
    if ind == 0:
        flag = False

print(res)
