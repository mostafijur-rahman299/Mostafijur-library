
add_num=lambda x,y:x+y
print(add_num(3,3))

bd_public=lambda name:"Bangladeshi citigen: "+name
print(bd_public('Mostafijur'))

print(*(lambda x,y: y[::-1])(input(), input().split()))
