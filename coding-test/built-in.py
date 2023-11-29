# 정수형
a = 2
b = 3

# 연산
print("a + b = " + str(a + b)) # 더하기
print(a - b) # 빼기
print(a * b) # 곱하기
print(a / b) # 나누기 + 소수점
# 몫만 반환하는 // 연산
print(a // b) # 나누기 정수부분만 표기

print(a ** b) # 지수 연산 : 2^3
print(a % b) # 나머지 연산(모듈러)
print(-a) # 부호 변경
print(abs(-a)) # 절대값

## 정수형 비교 연산
print(a == b) # 같은 값 비교
print(a != b)
print(a > b) # 2 > 3 ? False
print(a < b) # 2 < 3 : True
print(a >= b) # 같거나 더 큰가?
print(a <= b) # 같거나 더 작은가?

## 정수형 비트 연산: &, |, ^, ~, <<, >>
print(a & b)
print(a | b)
print(a ^ b)
print(~a) # NOT인데, 이건 계산해보기
print(a << 2) # 2의 제곱인 4를 곱한 값
print(a >> 1) # 2로 나눈 값

## 정수형 논리 연산
print(a and b) # 이거 좀 헷갈리는데, 마지막값인 b가 나옴.
print(a or b) # 이건 처음에 잡은 a가 나옴.
print(not a) # 이건 1이상인 값이 아니므로 0 -> False가 나옴.


# 부동 소수형: 소수 저장시 사용
## 사칙 연산
print("-" * 10 + "사칙 연산" + "-" * 10)
print(1.2 + 1.5)
print(1.2 - 1.5)
print(1.2 * 1.5)
print(10.0 / 3.2)

## 몫, 나머지, 제곱
print("-" * 10 + "몫, 나머지, 제곱" + "-" * 10)
print(10.0 // 3.1)
print(10.0 % 3.2) # 결과가 0.4가 아닌 이유는?
print(2.0 ** 3.2)

## 논리 연산
print("-" * 10 + "논리연산" + "-" * 10)
x = 0.5
y = 1.2
z = 2.0
print(x > y and y < z) # AND
print(x < y or y < z) # OR
print(not (x > y)) # NOT

# 앱실론 포함 연산 주의
## 이 앱실론: 표현 과정에서 오차. 이진법으로 표현.
## 일부 테스트 케이스 통과 못하는 이유이기도 하다.
import sys
# 앱실론 출력
print(sys.float_info.epsilon)

# 부동소수점 오차 검사
a = 0.2 + 0.2 + 0.2
b = 0.6

print(a - b)

# 검사: 오차 < 부동소수점이면 같은 값 출력
if abs(a - b) < sys.float_info.epsilon:
	print("a와 b 같다.")
else:
	print("a와 b 다르다.")


