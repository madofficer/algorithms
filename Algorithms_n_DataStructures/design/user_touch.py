class Touch:
    def __init__(self, t1, t2, x1, x2, y1, y2):
        self.t1 = t1
        self.x1 = x1
        self.y1 = y1

        self.t2 = t2
        self.x2 = x2
        self.y2 = y2


def touch_type(touch: Touch) -> int:
    time = touch.t2 - touch.t1
    d = ((touch.x2 - touch.x1) ** 2 + (touch.y2 - touch.y1) ** 2) ** 0.5
    if time < 100:
        return 1
    elif 100 <= time <= 1000 and d <= 50:
        return 2
    elif time > 1000 and d <= 50:
        return 3
    elif time >= 100 and d > 50:
        return 4


def read_input():
    for i in range(int(input())):
        t1, x1, y1 = map(int, input().split())
        t2, x2, y2 = map(int, input().split())
        touch = Touch(t1, t2, x1, x2, y1, y2)
        print(touch_type(touch))


if __name__ == "__main__":
    read_input()
