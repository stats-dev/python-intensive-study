def solution(numbers):
    ret = [ ] ## 빈 배열을 생성한다.

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            # 두 수 더한 결과를 새로운 배열 추가
            ret.append(numbers[i] + numbers[j])

    # 중복된 값 제거 후 오름차순 정렬
    ret = sorted(set(ret))
    return ret

print(solution(numbers=[2,1,3,4,1])) # [2, 3, 4, 5, 6, 7]