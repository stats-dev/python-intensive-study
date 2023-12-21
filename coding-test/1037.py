N = int(input())
k = map(int, input().split())

nList = [x for x in k]
nList.sort()
print(nList[0] * nList[len(nList)-1])