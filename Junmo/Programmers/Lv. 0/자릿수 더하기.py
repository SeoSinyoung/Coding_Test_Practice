# https://school.programmers.co.kr/learn/courses/30/lessons/120906
# 자릿수 더하기

def solution(n):
    answer = 0

    while True:
        answer += n % 10
        n //= 10
        if n == 0:
            break;

    return answer