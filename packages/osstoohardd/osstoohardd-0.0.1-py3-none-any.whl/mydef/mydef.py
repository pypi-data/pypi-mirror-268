import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

#경로의 역슬래쉬를 슬래쉬로 바꾼다
def toslash(data_path):
    a = rf"{data_path}"
    return a.replace("\\", '/')

#스터지스의 공식 사용
def stuges(df):
    k = np.ceil(1 + np.log2(len(df)))
    return k

#엑셀 데이터의 각 열마다 hist 생성
def eachhist(data_path):
    a = toslash(data_path)
    data = pd.read_excel(a)
    b = stuges(data)
    
    for col in data.columns:
        plt.hist(data[col], label=col, bins=int(b))
        plt.legend()
        plt.show()
        print('\n\n')
