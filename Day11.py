import matplotlib
print(matplotlib.__version__)

import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([0,6])
ypoints=np.array([0,250])
plt.plot(xpoints,ypoints)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
xpoints=np.array([1,8])
ypoints=np.array([3,10])
plt.plot(xpoints,ypoints,"o")
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Ayesha"]
marks=[80,90,75,95]
plt.plot(students,marks,color="red",linestyle="-.",marker="*")
plt.xlabel("students")
plt.ylabel("marks")
plt.title("student Result")
plt.grid()
plt.show()

import matplotlib.pyplot as plt
x=[1,2,3,4]
math=[80,85,90,95]
english=[75,78,82,88]
plt.plot(x,math,label="math")
plt.plot(x,english,label="english")
plt.legend()
plt.show()