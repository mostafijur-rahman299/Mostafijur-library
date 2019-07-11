# @Date:   2019-01-07T09:11:18+06:00
# @Last modified time: 2019-04-22T15:17:12+06:00

dict={'name':'sajib','age':34}

#items
for i,j in dict.items():
    print(i,j)

#values
for i in dict.values():
    print(i)
#keys
for k in dict.keys():
    print(k)


name_numbers=[input().split() for _ in range(3)]
phone_book={k:v for k,v in name_numbers}
print(phone_book)
