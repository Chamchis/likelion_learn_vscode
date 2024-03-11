# 사용자가 "시작"과 "종료"를 입력할 때까지의 시간을 측정하는 타이머 프로그램을 작성해보세요. 
# 사용자가 "시작"을 입력하면 타이머가 시작되고, 
# "종료"를 입력하면 타이머가 멈추며 경과 시간을 출력합니다.
import time
massage = input('시작을 입력하세요 : ')
if massage == '시작':
    start_time = time.time()
massage = input('종료를 입력하세요 : ')
if massage == '종료':
    end_time = time.time()
print(f'경과시간은 {end_time - start_time}초 입니다.')