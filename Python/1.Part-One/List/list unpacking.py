print(*input().split()[::-1])
print(' '.join(map(str, reversed(arr))))
print(*reversed(arr))

print(' '.join(str(x) for x in arr[::-1]))

[str(arr_temp) for arr_temp in input().strip().split(' ')][::-1]

print ((' ').join( arr ))

input()
a = list(map(int, input().split()))
print(*reversed(a))

print(*arr[ : : -1])

print(*reversed(arr))

print(*list(map(int, input().split()))[::-1])

print(*(lambda x,y: y[::-1])(input(), list(map(int, input().strip().split()))))
