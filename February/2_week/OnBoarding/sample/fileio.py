# 파일 읽기/쓰기
# C:\Users\junho\OneDrive\Desktop\workspace\sample\fileio.py
# f = open('literature\poem.txt','r', encoding='UTF-8')

# print(f.read())
# print(f.readline())
# print(f.readlines())

# f.close()

# with open('literature\poem.txt','r', encoding='UTF-8') as f:
#     print(f.read())

f = open('literature\poem.txt','a', encoding='UTF-8')

f.write("새로운 글이 작성되었습니다. ")

f.close()