""" 
10430 나머지
제한시간 1초

문제
(A+B)%C는 ((A%C) + (B%C))%C 와 같을까?

(A×B)%C는 ((A%C) × (B%C))%C 와 같을까?

세 수 A, B, C가 주어졌을 때, 위의 네 가지 값을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 A, B, C가 순서대로 주어진다. (2 ≤ A, B, C ≤ 10000)

출력
첫째 줄에 (A+B)%C, 둘째 줄에 ((A%C) + (B%C))%C, 셋째 줄에 (A×B)%C, 넷째 줄에 ((A%C) × (B%C))%C를 출력한다.

 """
a, b, c = list(map(int, input().split()))

w = (a + b) % c

x = ((a % c) + (b % c)) % c

y = (a * b) % c

z = ((a % c) * (b % c)) % c

print(w)
print(x)
print(y)
print(z)
