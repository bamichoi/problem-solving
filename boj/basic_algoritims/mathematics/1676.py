""" 
1676 팩토리얼 0의 개수
시간제한 2초

문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다. 
"""

n = int(input())


def factorial_recursive(num):
    return num * factorial_recursive(num - 1) if num > 1 else 1


f = factorial_recursive(n)
f = list(str(f))[::-1]

count = 0
i = 0
while f[i] == "0":
    if f[i] == "0":
        count += 1
        i += 1

print(count)
