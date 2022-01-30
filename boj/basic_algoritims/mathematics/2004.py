""" 
2004 조합 0의 개수
시간제한 2초

문제
 
$n \choose m$의 끝자리 $0$의 개수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 정수 $n$, $m$ ($0 \le m \le n \le 2,000,000,000$, $n \ne 0$)이 들어온다.

출력
첫째 줄에 
$n \choose m$의 끝자리 $0$의 개수를 출력한다.

 """

n, m = map(int, input().split())


def fiveCount(x):
    count = 0
    while x != 0:
        x = x // 5
        count += x
    return count


def twoCount(x):
    count = 0
    while x != 0:
        x = x // 2
        count += x
    return count


print(
    min(
        fiveCount(n) - fiveCount(m) - fiveCount(n - m),
        twoCount(n) - twoCount(m) - twoCount(n - m),
    )
)
