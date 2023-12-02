## 리스트 컴프리헨션

numbers = [1,2,3,4,5]
squares = [num**2 for num in numbers] # [1,4,9,16,25]

print(squares)

## 리스트 연관 메서드
## 이건 쓰자. len() 함수
## 처음 등장한 인덱스 index(), 없으면 -1 반환
## sort() : 정한 기준에 따라 리스트 데이터 정렬
## count() : 특정 데이터 개수 반환

examples = ["a","b","c","a","d","e","f"]
print(len(examples))
print(examples.index("b"))
print(examples.sort()) # None 왜 None? ['a', 'a', 'b', 'c', 'd', 'e', 'f']
print(examples) # sort 후에 나와야 프린트됨.
print(examples.count("a"))

## reverse true
examples.sort(reverse=True)
print(examples) # ['f', 'e', 'd', 'c', 'b', 'a', 'a']

## no sort but O(N^2)
import time # 시간을 잰다

def bubble_sort(arr): # 버블 정렬로 정렬
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] ## 이렇게 교체한다.
    return arr

def do_sort(arr): # sort() 함수로 배열 정렬하기
    arr.sort()
    return arr


## 시간 측정
def measure_time(func, arr):
    start_time = time.time() ## 시작 시간
    result = func(arr)
    end_time = time.time() ## 종료 시간
    return end_time - start_time, result

arr = list(range(10000)) ## 1만개 원소 리스트/배열

# 첫 코드 시간
buTime, buResult = measure_time(bubble_sort, arr)
print("첫번째 코드 실행 시간: ", format(buTime, ".10f")) #2초 걸림

## 두번째 코드
arr = list(range(10000))
rev_time, rev_result = measure_time(do_sort, arr)
print("두번째 코드 실행 시간:", format(rev_time, ".10f")) ## 책에 오타가좀 많다. 심각;

# 코드 결과가 동일한지 확인한다.
print("두 코드 결과 같아요? : ", buResult == rev_result) ## True


##2. 배열제어하기


