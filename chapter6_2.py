import requests
from bs4 import BeautifulSoup
import json
import time
import random

def extract_data_from_page(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    articles = soup.find_all('article', class_='item-box')  # 예시 클래스명, 실제로는 확인 후 수정 필요
    data = []

    for article in articles:
        title_tag = article.find('a', class_='tit-news')  # 예시 클래스명, 실제로는 확인 후 수정 필요
        summary_tag = article.find('p', class_='lead')  # 예시 클래스명, 실제로는 확인 후 수정 필요

        if title_tag and summary_tag:
            title = title_tag.text.strip()
            summary = summary_tag.text.strip()
            data.append({'Title': title, 'Summary': summary})
    
    return data

def fetch_page(url, proxies=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()  # HTTP 오류 발생 시 예외를 발생시킵니다.
        time.sleep(random.uniform(1, 3))  # 랜덤 지연
        return response
    except requests.RequestException as e:
        print(f"요청 오류: {e}")
        return None

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def crawl(urls, proxies=None):
    all_data = []
    
    for url in urls:
        print(f"수집 시작: {url}")
        response = fetch_page(url, proxies)
        
        if response:
            data = extract_data_from_page(response.content)
            all_data.extend(data)
            print(f"URL '{url}' 완료")
        else:
            print(f"URL '{url}'에서 데이터 수집 실패")
    
    return all_data


# 크롤링할 URL 리스트
urls = [
    "https://www.yna.co.kr/politics/index?site=navi_politics_depth01",
    "https://www.yna.co.kr/north-korea/all?site=navi_nk_depth01",
    "https://www.yna.co.kr/economy/index?site=navi_economy_depth01",
    "https://www.yna.co.kr/market-plus/index?site=navi_market_plus_depth01",
    "https://www.yna.co.kr/industry/index?site=navi_industry_depth01"
]

# 모든 페이지에서 데이터 수집
all_data = crawl(urls)

# 수집한 데이터를 JSON 파일로 저장
save_to_json(all_data, 'data.json')

print("데이터 수집 및 저장 완료.")
