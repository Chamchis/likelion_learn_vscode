# - **생일까지 남은 날짜 계산**
#     - 사용자로부터 생일을 입력받아, 현재 날짜로부터 다음 생일까지 남은 날짜를 계산하는 프로그램을 작성하세요.

from datetime import datetime, timedelta
birth_day = input('당신의 생일을 입력해주세요(XXXX-XX-XX) : ')
birth_day = datetime.strptime(birth_day,'%Y-%m-%d')
next_birthday = datetime(datetime.now().year + 1, birth_day.month, birth_day.day)
print(f'내년 생일은 {next_birthday.date()} 일 입니다.')
delta = next_birthday - datetime.now()
print(f'내년 생일까지 {delta.days} 일 남았습니다!')