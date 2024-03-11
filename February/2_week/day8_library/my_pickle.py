import pickle

data = {'a' : [i for i in range(10)],
        'b' : list('hello'),
        'c' :{True,False}}

print(data)
print(type(data))
with open('data,pickle','wb') as f:
    pickle.dump(data,f)
with open('data,pickle','wb') as f:
    data1 = pickle.load(f)

print(data1)
class A:
    name = 'good'
a = A()
with open('a.pickle','wb')as f:
    pickle.dump(a,f)
with open('a.pickle','rb') as f:
    aa = pickle.load()

print(aa.name)
