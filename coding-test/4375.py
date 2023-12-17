# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
# 각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.
while True:
    try:
        n = int(input())
    except:
        break
    i = 1 ## i는 자리수를 의미한다.
    num = 0 ## num은 0, 1, 11, 111 순으로 증가

    while True:
        num = num * 10 + 1 ## 1의자리로만 만든 것이다. n
        num = num % n ## n의배수 num = num % n즉, n의 배수 확인
        if num == 0:
            print(i)
            break ## 이 때 i는?
        i = i + 1 ## i가 하나씩 증가한다.


### 더 직관적인 코드
while True:
    try:
        n = int(input()) # 정수 n
    except:
        break

    num = 1    # 1로만 이루어진 수
    count = 1  # 자리수
    while True:
        if num % n != 0:  # n의 배수가 아니라면
            num = num * 10 + 1 # 1로만 이루어진 다음 수로 갱신
            count += 1         # 자리수 증가시키기
        else:      # n의 배수라면
            break  # 종료
    
    print(count) # 자리수 출력


