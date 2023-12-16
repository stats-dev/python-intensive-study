# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 각 자릿수가 모두 1로만 이루어진 n의 배수를 찾는 프로그램을 작성하시오.
# 각 자릿수가 모두 1로만 이루어진 n의 배수 중 가장 작은 수의 자리수를 출력한다.
while True:
    n = int(input())

    i = 1
    num = 0

    while True:
        num = num * 10 + 1 ## 1의자리로만 만든 것이다.
        num %= n ## n의배수 num = num % n 나머지 확인.
        if num == 0:
            print(i)
            break ## 이 때 i는?
        i += 1

    print(i)



