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

    # Рассчет стандартной ошибки для контроля и теста
    se_control = np.sqrt(conversion_control * (1 - conversion_control) / x_cnt)
    se_test = np.sqrt(conversion_test * (1 - conversion_test) / y_cnt)

    # Рассчет Z-статистики
    z_stat = (conversion_test - conversion_control) / np.sqrt(se_control**2 + se_test**2)

    # Рассчет p-значения
    p_value = stats.norm.sf(abs(z_stat))


    # Принятие решения об отклонении нулевой гипотезы
    if p_value < alpha:
        decision = True # Отклоняем нулевую гипотезу
    else:
        decision = False # Принимаем нулевую гипотезу 
    
    return False # Ваш ответ, True или False
