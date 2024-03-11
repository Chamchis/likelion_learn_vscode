import re

pattern = re.compile("ab")
print(pattern.match('ab'))
print(pattern.match('aab'))
print(pattern.match('abb'))
print('='*50)

# .을 이용한 매칭 : 줄바꿈을 제외한 다른 문자 하나를 의미

# '?'반복 : 0 또는 1회 반복
pattern = re.compile("a.b")
print(pattern.match('abb'))
print(pattern.match('ab'))
print(pattern.match('acb'))
print(pattern.match('a?b'))
print(pattern.match('a\nb'))

print('='*50)

# 단어 패턴 인식
pattern = re.compile("a?b")
print(pattern.match('bb'))
print(pattern.match('abb'))
print(pattern.match('aabb'))

print('='*50)

# search
pattern = re.compile("[a-z]+")
print(pattern.search('aabb'))
print(pattern.search('hello world'))
print(pattern.search('Hello world'))
print(pattern.search('3 hello world'))

print('='*50)

# findall
pattern = re.compile("[a-z]+")
print(pattern.findall('aabb'))
print(pattern.findall('hello world'))
print(pattern.findall('Hello world'))
print(pattern.findall('3 hello world'))

print('='*50)

# finditer
pattern = re.compile("[a-z]+")
pattern.finditer("2024 Like Lion Python backend")

outputs = pattern.finditer('2024 Like Lion Python backend')
for output in outputs:
    print(output)
print(output.span())
print(output.group())

print('='*50)

# 숫자
p = re.compile('\d+')
outputs = p.finditer('2024 Like Lion Python backend')
for output in outputs:
    print(output)

print('='*50)

p = re.compile('\d+.\d+')
outputs = p.finditer('pi : 3.141592 e : 2.78')
for output in outputs:
    print(output)

print('='*50)

# 한글 인식
data = """
안녕하세요!
멋사 제품을 항상 저를 만족시킵니다.
상당히 잘 사용하고 있는데 제가 멤버쉽에 잘 가입되었는지 궁금합니다.
제 이름은 홍길동이고 주민번호는 900101-1234567 이며 전화번호는 010-1234-5678입니다.
확인 부탁드립니다!
"""
p = re.compile('[가-힣]+')
print(p.finditer(data))

print('='*50)

# 옵션 IGNORECASE, I
p = re.compile("[a-zA-Z]+")
print(p.findall("aabb"))
print(p.findall("hello world"))
print(p.findall("Hello world"))
print(p.findall("3 hello world"))

print('='*50)

# 옵션 MULTILINE, M
txt = '''like lion
python backend
like tiger'''
p = re.compile("^like\s\w+",re.M) # [a-z]+
print(p.findall(txt))

print('='*50)

# 메타문자 : |
p = re.compile("hello|good")
print(p.match('good world'))

print('='*50)

# 메타문자 $ : 마지막
txt = '''like lion
python backend
like tiger'''

p = re.compile('tiger$')
print(p.search(txt))
print(re.search('tiger$', txt))

print('='*50)

# 메타문자 :\b: 공백
txt = '''like lion
lion good
python backend
like tiger'''

print(re.findall('\\blion', txt))

print('='*50)

# 그룹핑
p = re.compile('python+')
print(p.search('python'))
print(p.search('pythonnn'))
print(p.search('pythonpython'))

p = re.compile('(python)+')
print(p.search('python'))
print(p.search('pythonnn'))
print(p.search('pythonpython'))

print('='*50)

# 검색 조건 추가

p = re.compile('.+:')
m = p.search('http://www.naver.com')
print(m.group())

p = re.compile('.*[.](?!txt$)', re.M)
m = p.findall("""my_docs.txt
my_excel.xls
my_word.doc""")
print(m)

print('='*50)

# 문자열 바꾸기

p = re.compile('America|Britain|Canada|NewZealand')
m = p.sub('Empire','North America and South Britain and West Canada and East NewZealand')
print(m)