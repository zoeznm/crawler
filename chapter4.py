from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

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
            data.append((title, summary))
    
    return data

def scrape_category_pages(urls):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True로 설정하면 GUI 없이 실행됩니다.
        page = browser.new_page()
        
        all_data = []

        for url in urls:
            page.goto(url)
            page.wait_for_timeout(5000)  # 페이지 로딩 대기
            page_content = page.content()
            data = extract_data_from_page(page_content)
            all_data.extend(data)
            print(f"URL '{url}' 완료")
        
        browser.close()
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
all_data = scrape_category_pages(urls)

# 수집한 데이터 출력
for item in all_data:
    title, summary = item
    print(f"Title: {title}, Summary: {summary}")
