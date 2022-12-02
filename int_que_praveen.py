S = "12abc34fhsdfhs1223sdsd"
txt = "12abc34fhsdfhs1223sdsd"

l = [int(s) for s in txt.split() if s.isdigit()]
print(l)


num, res = 0,0
for i in S:
    if i >= "1" and i <= "9":
        num = num * 10 + int(i)
    else:
        num = 0
    res = max(res, num)

print(res)
