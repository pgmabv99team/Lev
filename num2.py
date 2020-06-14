import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (12, 8)

# Normal distributed x and y vector with mean 0 and standard deviation 1
# x = np.arange(0, 10, 1)
# y = x*2
x = np.random.normal(0, 1, 50)
y = np.random.normal(0, 1, 50)

plt.scatter(x, y)

plt.title('Generated Data')
plt.axis('equal')
plt.show()
