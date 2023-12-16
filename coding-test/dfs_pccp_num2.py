
# 초기화
answer = 0
def DFS(level, sum, ability, check):
    global answer
    n = len(ability) ## 학생 수
    m = len(ability[0]) ## 종목 개수

    if level == m:
        answer = max(answer, sum) ## 능력치 합의 최대 넣기
    else:
        for i in range(n):
            if check[i] == 0:
                check[i] = 1
                DFS(level+1, sum + ability[i][level], ability, check)
                check[i] = 0

def solution(ability):
    global answer
    check = [0] * len(ability)
    DFS(0, 0, ability, check)

    return answer
    


ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]
print(solution(ability))
