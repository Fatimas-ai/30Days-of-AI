import numpy as np
arr=np.array([5,10,15,20])
print(arr)

import numpy as np
arr=np.array([5,10,15,20])
print(arr[1])

import numpy as np
arr=np.array([
    [1,2],
    [3,4]
])
print(arr)

import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))

import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)

import numpy as np
marks=np.array([50,60,70,80])
print(marks.mean())

import numpy as np
arr=np.zeros((4,4))
print(arr)

import numpy as np
arr=np.ones((2,5))
print(arr)

import numpy as np
arr=np.random.randint(1,101,10)
print(arr)

import numpy as np
marks=np.array([80,90,75,88,95])
print("Marks:",marks)
print("Total marks:",marks.sum())
print("Average marks:",marks.mean())
print("Maximum marks:",marks.max())
print("Minimum marks:",marks.min())
print("Bonus marks:",marks+5)
print(marks.reshape(5,1))

import numpy as np
marks=np.array([78,85,92,67,88,95,73])
print("Marks:",marks)
print("Total marks:",marks.sum())
print("Average marks:",marks.mean())
print("Maximum marks:",marks.max())
print("Minimum marks:",marks.min())
print("Bonus marks:",marks+5)
print(marks.reshape(7,1))
print("Marks greater than 80:",marks[marks>80])
print("Last three elements:",marks[-4:])

import numpy as np
print(np.__version__)