print(input().strip().replace(' ', ''))


str = input()

[print(a) for a in str]

print('\n'.join(input()))



n=int(input())

print(f"{n} is {'eovdedn'[n&1::2]}")
print(f"{n} is {'even' if n % 2 == 0 else 'odd'}")