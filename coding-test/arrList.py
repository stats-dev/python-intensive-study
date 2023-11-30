# 리스트 데이터 추가

# append() : 맨끝 데이터 추가
myList = [1,2,3]
myList.append(4)
print(myList) # [1, 2, 3, 4]

# + 연산자는 여러 리스트를 맨끝 추가
myList = [1,2,3]
tList = myList + [4,5]
print(tList) # [1, 2, 3, 4, 5]

# insert(): 데이터 어디든 삽입
myList = [1,2,3,4,5]
myList.insert(2, 1234)
print(myList) # [1, 2, 1234, 3, 4, 5]

# 삭제
## pop() 특정 위치 데이터 팝팝!
myList = [1,2,3,4,5]
pop_ele = myList.pop(2) #반환하는 2번째 인덱스 값
print(f"전체 {myList}, 반환 {pop_ele}")
print(pop_ele)

## remove() 특정 데이터 삭제: 위치아님

