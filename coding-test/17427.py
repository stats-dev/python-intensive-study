## 약수의 합

# n = int(input())
# ## n 이하의 자연수를 구한다.
# nList = [x for x in range(1,n+1)]
# ## 각 자연수별 약수 리스트를 구한다.
# divList = []

## 시간초과1
# for k in nList:
#     for i in range(1, k+1):
#         if(k % i == 0):
#             divList.append(i)

# print(sum(divList))

## 시간초과2
# for k in nList:
#     for i in range(1, int(k**(1/2))+1):
#         if(k % i == 0):
#             divList.append(i)
#             if((i**2) != k):
#                 divList.append(k // i)

# print(sum(divList))

# n = int(input())
# print(sum(k * (n//k) for k in range(1, n+1)))

## 약수의 합2
N = int(input())

def g(N):
    result = 0
    for k in range(1, N+1):
        result += k * (N // k)
    
    return result

print(g(N))

## 느려서 빠른걸 가져왔다.
N, i, ans = int(input()), 1, 0
while i <= N:
  j = N//(N//i)
  ans += N//i * (i+j)*(j-i+1)//2
  i = j+1
print(ans)
