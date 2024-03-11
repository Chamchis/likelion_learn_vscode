# from .module_a import function_a
# from .module_b import function_b

# print('my_package 패키지의 init 파일 실행')
print('패키지가 초기화됩니다. ')

from . import module_a, module_b

# 패키지 수준의 변수 정의
package_variable = '이 변수는 패키지 전체에서 사용할 수 있어요'

# 공용 함수 정의
def common_function():
    print('my_package의 공용 함수입니다.')