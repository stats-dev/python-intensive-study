# 뮤터블 객체
mutaList = [1,2,3,4,5]
mutaList[4] = 6
print(mutaList) # 5번째 위치 값인 5를 6으로 수정


## 리스트: 인덱싱
mutaList = [1,2,4]
mutaList.append(6) # 값 추가
print(mutaList) # [1, 2, 4, 6]

del mutaList[1] # 값 삭제, 2번째 위치인 2가 사라집니다.
print(mutaList) # [1, 4, 6]

## 리스트: 슬라이싱
print("-"*10 + "리스트 슬라이싱" + "-"*10)
mutaList = [1,2,3,4,5]
print(mutaList[0:2]) # [1,2] 0부터 1번째까지
print(mutaList[1:]) # [2,3,4,5] 1번째 인덱스부터 끝까지
print(mutaList[:4]) # [1,2,3,4] 처음부터 3번째 인덱스
print(mutaList[-4:-1]) # [2,3,4] 이거 헷갈릴 수 있다.
## 음수는 -1부터 시작한다. -4부터 -2 인덱스(1부터 3)까지 출력합니다.

print("딕셔너리")
# 딕셔너리 초기화
muDict = {}

# 딕셔너리 삽입: 초기화를 수행해야 정상적으로 작동
muDict["a"] = 1
muDict["b"] = 2
muDict["c"] = 3

# 딕셔너리 출력
print(muDict) # {'a': 1, 'b': 2, 'c': 3}

## 딕셔너리 검색
exkey = "a"
if exkey in muDict:
    val = muDict[exkey]
    print(f"{exkey} : {val}") # a : 1
else:
    print(f"{exkey}는 없다.")


## 딕셔너리 예외처리
muDict = {"a": 1, "b": 2, "c": 3}

key = "d"

if key in muDict:
    print(f"val: {muDict[key]}")
else:
    print(f"'{key} is None in {muDict}")
    ## 'd is None in {'a': 1, 'b': 2, 'c': 3}

# 셋
print("셋")
testSet = set([1,2,3,3])
print(testSet) # {1, 2, 3}