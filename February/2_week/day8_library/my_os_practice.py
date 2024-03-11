import os

HOME_DIRECTORY = 'chdir_test'

# 홈 디렉터리로 이동
os.chdir(HOME_DIRECTORY)

# my_project 디렉터리 생성
os.mkdir('my_project')

# my_project 디렉터리 안으로 이동
os.chdir('my_project')

# README.md 파일 생성
with open('README.md', 'w') as f:
    f.write('my_project')