'''
abcd aacb adb
aaa aa

ans:[3,2]
3 comp btw 1st string all with 2nd string 1st
2 comp btw 1 st string all with 2nd string 2nd

1.First sort the given string in lex sir
2.find the smallest value frequency and give the comp to get ans
'''
def check_freq(l1,l2):
    res=[]
    for i in l2:
        count=0
        for j in l1:
            if(j<i):
                count+=1
        res.append(count)
    return res




s1=input('Enter the strings with , sep:').split(',')
s2=input('Enter the strings with , sep:').split(',')
s1f=[]
s2f=[]

#sort the indi strings in lex order
for i in range(0,len(s1)-1):
    s1[i]=''.join(sorted(s1[i]))
for j in range(0,len(s2)-1):
    s2[i]=''.join(sorted(s2[i]))
val=0
for i in s1:
    val=0
    for j in i:
        if j==i[0]:
            val=val+1
    s1f.append(val)
for i in s2:
    val=0
    for j in i:
        if j==i[0]:
            val=val+1
    s2f.append(val)
print(check_freq(s1f,s2f))




