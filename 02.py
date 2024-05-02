S = input()
N = int(input())
p = list(map(int, input().split()))

T = ""

for i in range(N):
    T += "a" * p[i] + " "

print((S) +" " + (T))
