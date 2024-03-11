#사용자가 입력한 숫자 범위(예: 1에서 100) 내에서 랜덤한 숫자를 생성하고,
#사용자가 이 숫자를 맞추는 간단한 숫자 맞추기 게임을 만들어보세요.

# 사용자가 숫자를 입력하게 해야 겠다
# 숫자 범위를 제한하는 기능이 필요하네
# 이 범위 안에서 랜덤한 숫자를 뽑아야 겠네
# 사용자가 숫자를 맞추기위해 입력해야 겠네
# 맞추면 맞췄다! 틀렸다를 알려줘야지
# 맞추면 끝내자
import random, time

num1 = int(input('첫번째 숫자를 입력하세요 : '))
num2 = int(input('두번째 숫자를 입력하세요 : '))

random_number = random.randint(num1, num2)

print('입력하신 범위에서 랜덤한 숫자가 생성되었습니다.')
inputnumber = int(input(f'{num1} ~ {num2} 사이의 숫자를 맞춰보세요 : '))

for i in range(5):
    input_number = int(input(f'{num1} ~ {num2} 사이의 숫자를 맞춰보세요: '))
    if input_number == random_number:
        print(f'축하합니다! 정답은 {random_number} 입니다.')
        break
    elif input_number > random_number:
        print('입력하신 숫자보다 작은 수입니다.')
        print(f'{4 - i}의 기회가 남아있습니다.')
    else:
        print('입력하신 숫자보다 큰 수입니다.')
        print(f'{4 - i}의 기회가 남아있습니다.')
    print('숫자를 맞추지 못했습니다.')