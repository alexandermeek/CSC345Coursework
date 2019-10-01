import numpy as np
import matplotlib.pyplot as plt

#Alexander Meek 5/10/18 911454
#Task 1.1
x = 345
y = 2 * x + 5
print(y)

print('Hello World')

def f(x, w, b):
    o = w * x + b
    return o
print(f(x, 2, 5))

#Task 1.2
B = [1, 3, 5, 8, 9]
for i in range(4, -1, -1):
    print(B[i])

def equals100(x):
    if x == 100:
        return True
    else:
        return False

print(equals100(59))
print(equals100(100))

myDictionary = {
    'data_name': 'myData',
    'data': np.random.randint(0, 5, (20, 3)),
    'labels': np.random.randint(0, 3, 20),
    }

print(myDictionary['data_name'])
print(myDictionary['data'])
print(myDictionary['labels'])

#Task 1.3
a = np.random.randint(0, 10, (2, 3))
b = np.random.randint(0, 10, (3, 4))
c = a@b
print(c[:, 0])

#Task 1.4
irisData = np.load('Iris_data.npy')
print(irisData.shape)

plt.scatter(irisData[:,0], irisData[:,1])

plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.title('Sepal size from Irises')

plt.show()
