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