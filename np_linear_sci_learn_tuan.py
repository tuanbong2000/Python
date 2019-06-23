import numpy as np
m=np.array([[49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68]]).T
# m is mass (kg) 2-array = matrix
h= np.array([147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183])
# h is hight (cm) 1-array
mbar=np.concatenate((np.ones(np.shape(m)),m*m,np.log(m)), axis=1)
# h= b0 + b1*m*m+ b2*log(m)

# Calculating weights of the fitting line

from sklearn import datasets, linear_model
# fit the model by Linear Regression
regr = linear_model.LinearRegression()
regr.fit(mbar, h) # in scikit-learn, each sample is one row
# Compare two results
print(regr.coef_)
#print("scikit-learn’s solution : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)
#print(regr.score(mbar, h))

import matplotlib.pyplot as plt
for i in range(0,m.shape[0]):
    plt.plot (m[i],h[i],'rx')
m_1=np.linspace(47,80,100)
plt.plot(m_1, regr.coef_[0] + regr.coef_[1]*m_1*m_1+regr.coef_[2]*np.log(m_1),'g')
plt.show()