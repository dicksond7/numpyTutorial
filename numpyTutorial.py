import numpy as np
from matplotlib import pyplot as plt



# Simple Array Definition
a = np.array([1,2,3])

# 2D Array
b = np.array([[1, 2], [3, 4]])

# 2D Array without implicit definition
# Define dimmension of array with ndmin
c = np.array([1, 2, 3, 4, 5], ndmin=2)

# Defining Array with certain datatype inside
d = np.array([1, 2, 3], dtype=float)


# Using the above arrays we can use attributes to learn more about the array as well as manipulate it

print(b.shape)

# Below we use both the shape attribute and reshape the function to reshape new matrix e
e = np.array([[1, 2], [3, 4], [5, 6]])
e.shape = (3, 2)
print(e.shape)

# Reset e to a 2x3 and use reshape instead
e = np.array([[1, 2], [3, 4], [5, 6]])
e.reshape(3, 2)
print(e.shape)
print(e.ndim)
print(e.itemsize)

# Using numpy for trigonometric calculations
f = np.array([0,30,45,60,90])
print(np.sin(f*np.pi/180))
print(np.cos(f*np.pi/180))
print(np.tan(f*np.pi/180))

# Using numpy to find floor and cieling of floats
g = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print(np.floor(g))
print(np.ceil(g))

# Using numpy to find nearest number rounded to a specific decimal place
h = np.array([1.0,5.55, 123, 0.567, 25.532])
print(np.around(h))
print(np.around(h, decimals = 1))
print(np.around(h, decimals = -1))

x = np.arange(1,10)
y = 2 * x + 5

plt.title("Matplotlib!!!")
plt.xlabel("This is the x-axis")
plt.ylabel("This is the Y-axis")
plt.plot(x,y)
#plt.show()

x1 = np.arange(-10,10)
y1 = x1 * x1 + 5
plt.plot(x1,y1,"+r")
#plt.show()


#bar graph
x3 = [5,8,10]
y3 = [12,16,6]

x4 = [6,9,11]
y4 = [6,15,7]

plt.bar(x3, y3, align = 'center')
plt.bar(x4, y4, color = 'g', align = 'center')
#plt.show()

m_list = [[4, 3], [-5, 9]]
A = np.array(m_list)
B = np.array([20, 26])
Z = np.linalg.solve(A, B)

print(Z)