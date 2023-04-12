import pandas as pd
import numpy as np
import scipy.stats as stats


chat_id = 263008738 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.1
    conversion_control = x_success / x_cnt
    conversion_test = y_success / y_cnt
    se_control = np.sqrt(conversion_control * (1 - conversion_control) / x_cnt)
    se_test = np.sqrt(conversion_test * (1 - conversion_test) / y_cnt)
    z_stat = (conversion_test - conversion_control) / np.sqrt(se_control**2 + se_test**2)
    p_value = stats.norm.sf((z_stat))
    if p_value < alpha:
        decision = True 
    else:
        decision = False 
    return decision 
