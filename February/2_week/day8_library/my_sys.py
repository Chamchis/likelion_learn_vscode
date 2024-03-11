import sys
script_name = sys.argv[0]
arguments = sys.argv[1:]
print(f"스크립트 이름: {script_name}, 인자: {arguments}")

ver = sys.version
print(ver)
exe = sys.executable
print(exe)
path = sys.path
print(path)
print(type(path))
sys.path.append('')