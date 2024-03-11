from collections import Counter, defaultdict, OrderedDict
colors = ['blue','blue','red','red','yellow']
count = Counter(colors)
print(count)

text = "파이썬 Counter 예제입니다. Counter는 텍스트에서 단어의 빈도를 분석하는 데 유용합니다."

# Counter 객체 생성
counter = Counter(text.split())

# 단어 빈도 출력
for word, count in counter.most_common():
    print(f"{word}: {count}")
    
d = defaultdict(int)
d['a'] += 1
print(d['a'])

# test_dict = {}
# test_dict['a'] +=1

d = defaultdict(list)
d[1].append((1,2,3,4,5,6))
d = defaultdict((lambda : 0))

d['key1'] += 1
print(d['key1'])

d = OrderedDict()
d['banana'] = 3
d['apple'] = 74
d['grape'] = 2
print(d)
