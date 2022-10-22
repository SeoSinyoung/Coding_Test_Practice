## 문자열 my_str과 n이 매개변수로 주어질 때,
# my_str을 길이 n씩 잘라서 저장한 배열을 return

def solution(my_str, n):
    answer = []
    cnt = len(my_str)//n  #
    for i in range(cnt) :
        answer.append(my_str[i*n:i*n+n])
    if len(my_str)%n != 0 :
        answer.append(my_str[(i+1)*n:])
    return answer