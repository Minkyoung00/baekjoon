N = int(input())
text = set()

for i in range(N):
    a = input()
    text.add(a)

for i in sorted(text, key=lambda x:(len(x),x)):
    print(i)