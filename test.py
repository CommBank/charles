s="abcd"

%matplotlib inline
import numpy as np
import matplotlib as mpl

mpl.style.use('ggplot')
mpl.style.available
x = np.linspace(0,10,500)
x = 2 * x



y = 11

mpl.pyplot.plot(x,np.sin(x))

import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s
