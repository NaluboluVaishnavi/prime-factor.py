def pf(n):
    ans = []
    i = 2
    while i<n:
        if n%1==0:
            ans.append(i)
            n = n//i
        else:
            i = i+1
    return ans    
ans = pf(6)
s = 0
a = [11,12,13,14,15,16]
for i in ans:
    s = s+ a[i]  
print(s)  
      
