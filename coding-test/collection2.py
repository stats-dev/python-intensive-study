# immutable 불변 객체
## 튜플

# 초기화
imTuble = (1,2,3,4,5)

## 튜플: 인덱싱, 슬라이싱같은 조회는 가능함
### 인덱싱
print(imTuble[0])
print(imTuble[1])
print(imTuble[-1])

### 슬라이싱
print(imTuble[0:1])
print(imTuble[:2])
print(imTuble[2:])
print(imTuble[-1:-2]) # () 음수 인덱스 슬라이싱 불가?

print("문자열")
## 문자열

# 초기화
str1 = "test"
str2 = 'test'

## 추가, 삭제: 수정이 아니라 새 객체 반환
str1 = "test"
str1 += "graph"
print(str1)

## 수정과 삭제: replace()로 가능
str2 = "test"
str3 = str2.replace("t", "t1")
str2 = str2.replace("t", "") # t 모두 제거
print(str3) # t1est1
print(str2) # es