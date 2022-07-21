arr=["바나나","딸기","바나나","사과"]
d={i:0 for i in arr}

for i in arr:
    if i =='바나나':
        d[i]+=1
print(d.get("바나나"))