from multiprocessing import Process, Value, Array

def process_function():
    print("프로세스 실행 중")

if __name__ == '__main__':
    process = Process(target=process_function)
    process.start()
    process.join()  # 프로세스가 종료될 때까지 기다림

def work(id):
    print(f'Process {id} working...')

processes = [Process(target=work, args=[i,]) for i in range(2)]

for p in processes:
    p.start()
for p in processes:
    p.join()

def add_one(number,array):
    number.value += 1
    for i in range(len(array)):
        array[i] += 1
number = Value('i',0)
array = Array('i',range(5))
processes = [Process(target=add_one, args=(number,array)) for _ in range(2)]

for p in processes:
    p.start()
for p in processes:
    p.join()
print(f'number : {number.value}')
print(f'array : {list(array)}')