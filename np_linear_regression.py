import numpy as np
m=np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
# m is mass (kg) 2-array = matrix
h= np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183])
# h is hight (cm) 1-array
mbar=np.concatenate((np.ones(np.shape(m)),m), axis=1)

# Calculating weights of the fitting line
A=np.dot(mbar.T,mbar)
b=np.dot(mbar.T,h)
x= np.dot(np.linalg.pinv(A),b)
print(x)

# lap ham tim chieu cao dua vao can nang
def chieucao(m1):
    return x[1]*m1+x[0]


print('nguoi co can nang:', 55, 'co chieu cao la:',chieucao(55) )
print('nguoi co can nang:', 60, 'co chieu cao la:',chieucao(60) )

m1=np.array([50,63,75])
print(m1,'co chieu cao la:',chieucao(m1), sep="\n")

import matplotlib.pyplot as plt
for i in range(0,m.shape[0]):
    plt.plot (m[i],h[i],'rx')
m_1=np.linspace(47,80,100)
plt.plot(m_1, x[1]*m_1+x[0],'g')
plt.show()