# https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 아이스 아메리카노

def solution(money):
    answer = []

    answer.append(money // 5500)
    answer.append(money % 5500)

    return answer