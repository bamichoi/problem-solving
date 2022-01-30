""" 
9613 GCD 합
시간제한 1초

문제
양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다. 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

출력
각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.
 """

import math

t = int(input())
for _ in range(t):
    sum = 0
    arr = list(map(int, input().split()))
    k = arr.pop(0)
    for i in range(k):
        for j in range(k):
            if i < j:
                gcd = math.gcd(arr[i], arr[j])
                sum += gcd
    print(sum)
