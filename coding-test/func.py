def fn_name(param1, param2, paramN):
    result = param1 + param2 + paramN
	# 실행 코드
    return result # 반환값

# 호출
def add(n1, n2):
    result = n1 + n2
    return result

print("함수 호출 후 결과 출력: add(10,5)")
ret = add(10,5)
print('add(10,5): ', ret) # add(10,5):  15


## 람다식: 한 번 실행, 익명함수, 타 함수의 인수
lambda x, y: x + y

## 람다식 사용
### 2가지 변수 차조, 변수(a,b) 등으로 호출하여 실행 가능
add = lambda x,y: x+y
print(add(5,4))

### 인수로 넘기기 : map()
num = [1,2,3,4,5]
sq = list(map(lambda x: x**2, num)) #이렇게 람다식을 map 안에 넣어서 넘겨버립니다.
#그걸 리스트로 다시 묶으면, 새리스트가 반환됩니다.
#묶지 않으면 그냥 주소값만 나오네요. map 자체의 객체 주소값만 있답니다. list()로 묶기
print(sq)


## 조기 반환: early return
def total_price(quantity, price):
    total = quantity * price # total이 100보다 크면, 조기반환
    if total > 100:
        return total * 0.8
    return total # 이건 쓰지 않게 되겠죠.

print(total_price(4, 50)) # 160.0이 나온다.


## 보호 구문: guard clauses
def cal_avg(nums):
    if nums is None: # 값이 없으면 종료, 예외
        return None
    
    if not isinstance(nums, list): # nums가 리스트 형태가 아니면 종료
        return None
    
    if len(nums) == 0: # nums 길이가 0이면 종료
        return None
    
    total = sum(nums)
    avg = total / len(nums)
    return avg

print(cal_avg([])) # None

print("합성함수")
# 4를 더한다.
def add_four(x):
    return x + 4

# 제곱한다.
def square(x):
    return x * x

composed_function = lambda x: square(add_four(x))
print(composed_function(4)) ## 4에 4를 더한 8을 제곱한 64가 나온다.