import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st

chat_id = 586939927 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    pv= st.cramervonmises_2samp(x,y)[1]
    print(pv)
    if pv > 0.01:
        return False
    else:
        return True
