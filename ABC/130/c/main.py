w, h, x, y = map(int, input().split())

answer = w*h/2
judge = 1 if w/2 == x and h/2 == y else 0

print(answer, judge)
