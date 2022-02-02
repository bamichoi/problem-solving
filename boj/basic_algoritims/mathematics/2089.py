""" 
2089 -2진수
시간제한 2초

문제
-2진법은 부호 없는 2진수로 표현이 된다. 2진법에서는 20, 21, 22, 23이 표현 되지만 -2진법에서는 (-2)0 = 1, (-2)1 = -2, (-2)2 = 4, (-2)3 = -8을 표현한다. 10진수로 1부터 표현하자면 1, 110, 111, 100, 101, 11010, 11011, 11000, 11001 등이다.

10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성하시오.

입력
첫 줄에 10진법으로 표현된 수 N이 주어진다.

출력
-2진법 수를 출력한다.

제한
-2,000,000,000 ≤ N ≤ 2,000,000,000 
"""

num = int(input())

reminders = []

if not num:
    print("0")
    exit()

while num:
    if num % -2 == 0:
        num = num // -2
        reminders.append("0")
    elif num % -2 != 0:
        num = num // -2 + 1
        reminders.append("1")

reminders.reverse()
print("".join(reminders))
