import requests
from bs4 import BeautifulSoup

# 1. 웹 페이지의 HTML 데이터를 가져오기
url = "https://www.yna.co.kr/"
response = requests.get(url)
html = response.text

# 2. BeautifulSoup을 사용하여 HTML 파싱하기
soup = BeautifulSoup(html, 'html.parser')

# 3. 필요한 데이터 추출하기
# HTML 구조에 맞게 태그와 클래스 수정
products = soup.find_all('article', class_='item-box')

for product in products:
    title_tag = product.find('a', class_='tit-news')
    contents_tag = product.find('p', class_='lead')

    if title_tag and contents_tag:
        title = title_tag.text.strip()
        contents = contents_tag.text.strip()
        print(f"Product: {title}, Contents: {contents}")
    else:
        print("Tag not found")
