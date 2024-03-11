from datetime import datetime, timedelta, pytz
now = datetime.now()
print(now)

start_day = datetime(2024,2,19,9)
print(start_day)

now = datetime.now()
print(now)

formatted = now.strftime('%Y-%m-%d %H-%M-%S')
print(formatted)
print(type(formatted))

# 문자열로부터 날짜와 시간 파싱
date_str = "2024년-02-28day 01:37:54"
dt = datetime.strptime(date_str,"%Y년-%m-%dday %H:%M:%S")
print(dt)

print(start_day)
today = datetime.now()
delta = today - start_day
print(delta.days)

one_week_later = now + timedelta(weeks=1)
print(one_week_later)

timezone = pytz.timezone('Asia/Seoul')
seoul_time = datetime.now(timezone)
print(seoul_time)