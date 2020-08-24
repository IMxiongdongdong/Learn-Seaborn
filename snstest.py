import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
    plt.show()


sns.set()
sinplot()

# import matplotlib.pyplot as plt
# plt.style.use('classic')
# import numpy as np
# import pandas as pd
# import seaborn as sns
#
# rng = np.random.RandomState(0)
# x = np.linspace(0, 10, 500)
# y = np.cumsum(rng.randn(500, 6), 0)
#
# sns.set()
# plt.plot(x, y)
# plt.legend('ABCDEF', ncol=2, loc='upper left')
# plt.show()