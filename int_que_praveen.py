S = "12abc34fhsdfhs1223sdsd"
txt = "12abc34fhsdfhs1223sdsd"
# l = [int(s) for s in list(txt) if s.isdigit()]
# print(l)


num, res = 0,0
temp = ""
res2 = "0"
for i in S:
    if i >= "1" and i <= "9":
        temp += i
        num = num * 10 + int(i)

    else:
        num = 0
        temp = "0"
    res = max(res, num)
    res2 = max(int(res2), int(temp))

print(res)
print(res2)
