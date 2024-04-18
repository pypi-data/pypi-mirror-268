import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 데이터 파일 읽기
def read_data(file_path):
    # 파일 확장자 확인
    if file_path.lower().endswith('.xlsx') or file_path.lower().endswith('.xls'):
        df = pd.read_excel(file_path)
    elif file_path.lower().endswith('.csv'):
        df = pd.read_csv(file_path)
    else:
        raise ValueError("지원하지 않는 파일 형식입니다.")

    return df

# 막대그래프
def show_bar(df, save_path=None):
    # 폰트 설정
    plt.rcParams['font.family'] = 'Malgun Gothic'

    plt.figure(figsize=(10, 6))
    df.plot(kind='bar', figsize=(10, 6))
    plt.title("title")
    plt.xlabel('x')
    plt.ylabel('y')

    # 그래프 화면 표시
    plt.show()

    # 이미지 저장
    if save_path:
        plt.savefig(save_path)

# 데이터 열의 평균
def mean_data(df, column_name):
    values = df[column_name].values

    # numpy를 사용하여 평균 계산
    mean_value = np.mean(values)

    return mean_value
