# 고객 문의 사항 예시
data = """
안녕하세요!
멋사 제품은 항상 저를 만족시킵니다.
상당히 잘 사용하고 있는데 제가 멤버쉽에 잘 가입되었는지 궁금합니다.
제 이름은 호날두이고 주민번호는 900101-1234567 이며 전화번호는 010-1234-5678입니다.
확인 부탁드립니다!
"""

# 900101-1234567 -> 900101-*******
# 단어 단어를 쪼개서 그 부분이
# 14개의 문자로 이어진 부분이 있으면
# - 구분하고 앞부분, 뒷부분이 숫자이면
# 주민등록번호라고 의심을 해서
# 마스킹을 하겠습니다.
result =[]
tmp = ''
for line in data.split("\n"): # \n : 개행문자. 줄바꿈.
  word_result = []
  for word in line.split(' '):
    if len(word) == 14 and word[:6].isdigit() and word[-7:].isdigit():
      word = word[:6] + '-*******'
    word_result.append(word)
  result.append(' '.join(word_result))
print('\n'.join(result))

