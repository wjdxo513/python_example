#아나콘다를 설치한 후에 패스가 걸려있으면 정상적으로 실행됨
import numpy as np
import matplotlib.pyplot as plt 
from pylab import show 

x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)

show()


