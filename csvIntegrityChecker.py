import pandas as pd

# 데이터 로드 및 불필요한 값 제거
df = pd.read_csv('C:/Users/user/Desktop/dataCheck/expdata/result_01.csv')
df = df.drop(columns=['Unnamed: 0'])


# 31번째 열 확인 및 31번째 열 변수로 지정 - 라벨 값을 확인하는 것이므로
global row_31
row_31 = df.iloc[31,:]

# index_i 리스트 만들기
for i in range(1,20):
    globals()['index_{}'.format(i)] = row_31[row_31 == i].index.tolist()

# 인덱스 개수 확인 - index_1의 개수는 1, index_2 ~ index_11까지는 모두 20개가 나오면 정상
for i in range(1, 12):
    print("length of index_",i, " = ", len(globals()['index_{}'.format(i)]))
