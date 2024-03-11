# 현재 시간 얻기
import time
current_time = time.time()
print(current_time)
local_time = time.localtime(current_time)
print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))

for i in range(3):
    print(f'{i+1}번째 메시지')
    time.sleep(1)

start_time = time.time()
time.sleep(2)
end_time = time.time()
print(f'프로그램 실행 시간 : {end_time - start_time}')