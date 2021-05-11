#1. find 's' in mississippi
s="mississippi"
cnt=0
for i in s:
    if i=='s':
        cnt+=1
print(cnt)

# 2. uncommon words
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
cnt={}
for word in A.split(" "):
    cnt[word]=cnt.get(word,0)+1
for word in B.split(" "):
    cnt[word] = cnt.get(word,0) + 1

print([word for word in cnt if cnt[word]==1])




# 3. replace none with next element in the list

def nonList(Lst):
    for i in range(len(Lst)):
        if Lst[i] is None:
            Lst[i]=Lst[i+1]
    return Lst

Lst= [None, None, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5]
print(nonList(Lst))

#Find uncommon characters of the two strings
tr1 = 'characters'
str2 = 'alphabets'
s1=set(tr1)
s2=set(str2)
ls1=list()
ls2=list()
finalList=list()
for i in s1:
    ls1.append(i)
for  j in s2:
    ls2.append(j)

for ele in ls1:
    if ele not in ls2:
        finalList.append(ele)
for ele in ls2:
    if ele not in ls1:
        finalList.append(ele)


print(str(finalList))



# 2. Given a ´dictionary, print the key for nth highest value present in the dict.
# If there are more than 1 record present for nth highest value then
# sort the key and print the first one.


lst=[1,2,3,2,3,4,5,6,6,5,3,3,2]
dic= dict()
for ele in lst:
    if ele in dic:
        dic[ele]+=1
    else:
        dic[ele]=1
print(dic)
maxVal=max(dic.values())
print('Max Val',maxVal)
for k,v in dic.items():
    if k==maxVal:
        print('nth highest value:',v)


#Given two sentences, you have to print the words those are not present in either of the sentences.
# (If one word is present twice in 1 st sentence but not present in 2 nd
# sentence then you have to print that word too)

A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
ls1=A.split(" ")
ls2=B.split(" ")
finalLst=list()
for ele in ls1:
    if ele not in finalLst:
        finalLst.append(ele)
for ele in ls2:
    if ele not in finalLst:
        finalLst.append(ele)
print(finalLst)