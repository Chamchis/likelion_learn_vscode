from multiprocessing import Pool

def square(n):
    return n**2

if __name__ == '__main__':
    with Pool(4) as p:
        results = p.map(square, range(10))
    print(results)