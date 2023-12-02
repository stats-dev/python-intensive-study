## 정수 배열을 정렬해서 반환
## 100000이상이면, 3초 제한 시간이면 N^2 dkfrhflwma tkdydgkf tn djqtek.
## 정답 코득가 아주 짧다.
## 주목할 점: sort() 메서드가 리스트 원본 자체의 값을 바꾼다.
def solution1(arr1):
    arr1.sort()
    return arr1

## list(sort()): 이렇게 하면 원본은 그대로 두고, 바꾼다.
def solution2(arr2):
    sorted_list = list(sorted(arr2)) ## 이거 작동 안함
    return sorted_list
    
def solution3(lst):
  unique_lst = list(set(lst)) #  중복값 제거
  unique_lst.sort(reverse=True) #  내림차순 정렬 
  return unique_lst
  


## 저자의 테스트 코드: TEST 코드 입니다. 주석을 풀고 실행시켜보세요
print("sol1:arr.sort()")
print(solution1([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
print(solution1([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution1([1,6,7])) # 반환값 : [1, 6, 7]

print("sol2:list(sorted(arr))")
print(solution2([1,-5,2,4,3])) # 반환값 : [-5, 1, 2, 3, 4]
print(solution2([2,1,1,3,2,5,4])) # 반환값 : [1, 1, 2, 2, 3, 4, 5]
print(solution2([1,6,7])) # 반환값 : [1, 6, 7]

print("sort(reverse=True)")
print(solution3([1,-5,2,4,3])) # 반환값 : [4, 3, 2, 1, -5]
print(solution3([2,1,1,3,2,5,4])) # 반환값 : [5, 4, 3, 2, 1]
print(solution3([1,6,7])) # 반환값 : [7, 6, 1]
