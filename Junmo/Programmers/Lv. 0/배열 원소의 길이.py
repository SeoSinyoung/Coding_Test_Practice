# https://school.programmers.co.kr/learn/courses/30/lessons/120854
# 배열 원소의 길이

def solution(strlist):
    answer = []

    for str in strlist:
        answer.append(len(str))

    return answer