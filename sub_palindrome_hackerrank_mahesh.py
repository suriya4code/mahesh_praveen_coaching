s = "mokkori"
l = len(s)

def is_palindrome(a):
    return a == a[::-1]

res = []
for i in range(l):
    for j in range(i+1,l+1):
        if is_palindrome(s[i:j]):
            res.append(s[i:j])

print(len(set(res)))
