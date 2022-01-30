""" 

1978 소수 찾기
시간제한 2초

문제
주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

입력
첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

출력
주어진 수들 중 소수의 개수를 출력한다.

 """

n = int(input())
numbers = list(map(int, input().split()))
pn = 0
for number in numbers:
    other = 0
    if number > 1:
        if number == 2:
            pn += 1
        else:
            for i in range(2, number):
                if number % i == 0:
                    other += 1
            if other == 0:
                pn += 1
print(pn)
