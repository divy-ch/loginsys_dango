arr = [1,5,4,2,3]

sbarr = []
sbsbarr = []
i=0
while i<len(arr):
    j=i
    while j<len(arr):
        k=i
        while k<=j:
            sbsbarr.append(arr[k])
            k+=1
        sbarr.append(sbsbarr)
        sbsbarr = []
        j+=1
    i+=1


sumsbarr =[]
for i in range(len(sbarr)):
    if len(sbarr[i])%2!=0:
        sumsbarr.append(sum(sbarr[i]))
print(sum(sumsbarr))
