# 사용자가 디렉토리 지정
# 확장자 지정
# 해당 디렉토리의 해당 확장자 파일 목록을 출력
import glob, os
dir_path = input('검색할 디렉터리를 입력하세요 : ')
exp_file = input('검색할 확장자를 입력하세요 : ')
e_list = glob.glob(os.path.join(dir_path, f'*{exp_file}'))