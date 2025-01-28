n = int(input())

class result:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

cnt = []
for _ in range(n):
    date, day, weather = input().split()
    cnt.append(result(date, day, weather))

cnt.sort(key=lambda x: x.date)

for i in range(n):
    if cnt[i].weather == 'Rain':
        print(cnt[i].date, cnt[i].day, cnt[i].weather)
        break