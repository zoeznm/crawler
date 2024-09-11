import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# JSON 파일에서 데이터 로드
data = pd.read_json('api_joke.json')

# 데이터 기본 탐색
print(data.head())
print(data.describe())
print(data.info())

# 시각화 스타일 설정
sns.set(style="whitegrid")

# 예시: 'created_at'을 이용한 시각화
plt.figure(figsize=(10, 6))
sns.histplot(data['created_at'].astype('int64') // 10**9, bins=30, kde=True)  # 'created_at'을 타임스탬프로 변환하여 사용
plt.title('Distribution of Created At Timestamps')
plt.xlabel('Timestamp (seconds)')
plt.ylabel('Frequency')
plt.show()

# 상관관계 히트맵 시각화 (숫자형 열이 있는 경우)
corr = data[['created_at', 'updated_at']].apply(lambda x: x.astype('int64') // 10**9).corr()
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# 예시: 시계열 데이터 'created_at'과 'updated_at'을 사용하여 시각화
plt.figure(figsize=(12, 6))
plt.plot(data['created_at'], data['updated_at'], marker='o')
plt.title('Created At vs Updated At')
plt.xlabel('Created At')
plt.ylabel('Updated At')
plt.xticks(rotation=45)
plt.show()

# 기초 통계량 (예시로 'created_at' 열 사용)
print(data['created_at'].mean())
print(data['created_at'].median())
print(data['created_at'].std())

# 카테고리별 그룹화 후 평균 계산 (범주형 열이 있는 경우)
grouped_data = data.groupby('categories').mean()
print(grouped_data)
