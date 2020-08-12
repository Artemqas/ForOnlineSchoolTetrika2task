import collections

#Т.к файл удалось скачать только в формате "<host>" "<ip>" "<page>"
# то в 11 строке используется другой параметр в split

f = open('NewText.txt', mode = 'r', encoding = 'UTF-8')
names = f.readlines()
newlist = []
mainlist = []
for i in names:
    newlist.append(i.split('" "'))
for i in newlist:
    mainlist.append(i[1])
del newlist, names
#c = collections.Counter() --- здесь считает все ip-адреса, которые встречались
#for word in mainlist:     ---
    #c[word] += 1          ---
#print(c)
mostCommon5 = collections.Counter(mainlist).most_common(5)
print(mostCommon5)
