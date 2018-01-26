if a == 0 and b == 360:
    print(c + 360)
if a == 0 and b <= 90:
    print(b - a)
if a == 0 and b == 270:
    print(c + 360)
if a == 0 and b == 210:
    print((b - a - 360) * -1)
if a == 0 and b == 240:
    print((b - a - 360) * -1)
if a == 0 and b == 300:
    print((b - a - 360) * -1)
if a == 0 and b == 330:
    print((b - a - 360) * -1)
if a == 0 and b <= 180 and b > 91:
    print(b - a)
if a == 82.5 and b >= 90 and b < 180:
    print(b - a)
if a == 82.5 and b >= 180 and b <= 210:
    print(b - a)
if a >= 82.5 and b > 239 and b <= 270:
    print(b - a)
if a == 82.5 and b >= 300 and b <= 330:
    print((b - a - 360) * -1)
if a == 82.5 and b <= 60 and b >= 30:
    print((b - a) * -1)
if a > 0 and a <= 80 and b == 30:
    print((b - a))
if a > 0 and a <= 180 and b == 60:
    print("test algo1")
    # if a == 82.5 and b >= 179:
    #     print(b -a)