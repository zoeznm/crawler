import pandas as pd
import json
import matplotlib.pyplot as plt  # matplotlib 불러오기
import seaborn as sns  # seaborn 불러오기

# JSON 파일 로드
with open('starwars.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  # JSON 데이터를 딕셔너리로 로드

# 데이터 확인
print(data)

# 데이터프레임으로 변환할 수 있는 부분 선택
df = pd.DataFrame([data])  # 단일 객체이므로 리스트로 감싸서 DataFrame으로 변환

# 데이터 기본 탐색
print(df.head())
print(df.describe())
print(df.info())

# 시각화 스타일 설정
sns.set(style="whitegrid")

# 예시: 'created' 열을 시각화
df['created_at'] = pd.to_datetime(df['created'])
plt.figure(figsize=(10, 6))
sns.histplot(df['created_at'].astype('int64') // 10**9, bins=30, kde=True)  # 'created_at'을 타임스탬프로 변환하여 사용
plt.title('Distribution of Created At Timestamps')
plt.xlabel('Timestamp (seconds)')
plt.ylabel('Frequency')
plt.show()

# 상관관계 히트맵 시각화 (숫자형 열이 있는 경우)
df['edited_at'] = pd.to_datetime(df['edited'])  # 'edited' 열도 시계열로 변환
corr = df[['created_at', 'edited_at']].apply(lambda x: x.astype('int64') // 10**9).corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# 예시: 시계열 데이터 'created_at'과 'edited_at'을 사용하여 시각화
plt.figure(figsize=(12, 6))
plt.plot(df['created_at'], df['edited_at'], marker='o')
plt.title('Created At vs Edited At')
plt.xlabel('Created At')
plt.ylabel('Edited At')
plt.xticks(rotation=45)
plt.show()

# 기초 통계량
print(df['created_at'].mean())
print(df['created_at'].median())
print(df['created_at'].std())
