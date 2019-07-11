sum=0
list=[2,34,5,6,6,3,'sajib',3,4,5,6,False]
for num in list:
    if type(num) == str or type(num) == bool:
        continue
    sum+=num
print(sum)
